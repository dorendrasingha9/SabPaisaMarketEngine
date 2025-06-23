import streamlit as st
import pandas as pd
import time
import openai
from PIL import Image
import os
from ai_pitch_generator import generate_pitch
from data_model import load_data, save_data, COLUMNS
from report_export import generate_xml_report

# Load logo in sidebar
if os.path.exists("sp.png"):
    logo = Image.open("sp.png")
    with st.sidebar:
        st.image(logo, width=180)
else:
    with st.sidebar:
        st.warning("⚠️ Logo not found.")

st.title("SabPaisa Market Intelligence Engine (MVP)")

# Upload & generate
st.subheader("Upload Prospect Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
if data_file:
    df = load_data(data_file)
    st.dataframe(df)

    if st.button("Generate Pitches"):
        st.subheader("Generating pitches... please wait.")
        pitches, errors = [], []

        for i, row in df.iterrows():
            retries = 3
            for attempt in range(retries):
                try:
                    pitch = generate_pitch(row.to_dict())  # ✅ FIXED HERE
                    pitches.append(pitch)
                    st.markdown(f"✅ **{row['Name']}**: Pitch generated")
                    time.sleep(1.2)
                    break
                except openai.RateLimitError:
                    if attempt < retries - 1:
                        time.sleep(3)
                    else:
                        st.error(f"⚠️ Rate limit hit. Skipping: {row['Name']}")
                        pitches.append("Rate limit error")
                        errors.append(i)
                except Exception as e:
                    st.error(f"❌ Error for {row['Name']}: {str(e)}")
                    pitches.append("Error")
                    errors.append(i)
                    break

        while len(pitches) < len(df):
            pitches.append("Pitch not generated")
            errors.append(len(pitches)-1)

        df["Pitch"] = pitches
        save_data(df, "prospects_with_pitch.csv")
        if errors:
            st.warning(f"⚠️ {len(errors)} rows had issues.")
        else:
            st.success("✅ All pitches processed.")

        with open("prospects_with_pitch.csv", "rb") as file:
            st.download_button("📤 Download Pitch Report", file, "pitch_report.csv", "text/csv")

# Manual input
st.subheader("Add Prospect Manually")
with st.form("prospect_form"):
    inputs = {col: st.text_input(col) for col in COLUMNS}
    if st.form_submit_button("Add Prospect"):
        new_df = pd.DataFrame([inputs])
        try:
            existing = pd.read_csv("prospects_with_pitch.csv")
        except:
            existing = pd.DataFrame(columns=COLUMNS + ["Pitch"])
        try:
            pitch = generate_pitch(inputs)
            time.sleep(1.2)
        except:
            pitch = "Pitch not generated"
        new_df["Pitch"] = pitch
        combined = pd.concat([existing, new_df], ignore_index=True)
        save_data(combined, "prospects_with_pitch.csv")
        st.success("Added.")

# Show table
st.subheader("Prospect List with Pitches")
try:
    table = pd.read_csv("prospects_with_pitch.csv")
    st.dataframe(table)
    with open("prospects_with_pitch.csv", "rb") as file:
        st.download_button("📤 Download Current Report", file, "pitch_report.csv", "text/csv")
except:
    st.info("No data yet.")

# Target planning
st.subheader("Target Planning (Quarter-wise)")
quarters = ["Q1", "Q2", "Q3", "Q4"]
gmvs = [st.number_input(f"{q} GMV (Cr)", 0.0) for q in quarters]
signups = [st.number_input(f"{q} Signups", 0) for q in quarters]
if st.button("Save Targets"):
    pd.DataFrame({
        "Quarter": quarters,
        "GMV": gmvs,
        "Merchant Signups": signups
    }).to_csv("targets.csv", index=False)
    st.success("Targets saved.")

st.subheader("Target Dashboard")
try:
    st.dataframe(pd.read_csv("targets.csv"))
except:
    st.info("No targets yet.")

# Export report
if st.button("Generate XML Report"):
    path = generate_xml_report()
    if path:
        with open(path, "rb") as f:
            st.download_button("📥 Download XML Report", f, "smipe_report.xml", "application/xml")
