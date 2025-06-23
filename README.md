# SabPaisa SMIPE MVP 🚀

This is the complete source code for **SabPaisa Market Intelligence Engine (SMIPE MVP)** — a Streamlit app that helps generate personalized sales pitches, plan targets, and export structured reports.

## 📦 Features

✅ Upload CSV with prospect data  
✅ Generate personalized pitches using OpenAI  
✅ Add prospects manually  
✅ Track GMV & Signups quarter-wise  
✅ Export report as XML  
✅ Download reports as CSV  
✅ Display SabPaisa logo in sidebar  
✅ Safe error handling & retry logic

## 📁 Project Structure

```
sabpaisa-smipe/
├── app.py                 # Streamlit app main file
├── ai_pitch_generator.py # OpenAI-based pitch generation
├── data_model.py         # Data load/save utilities
├── report_export.py      # XML report generation
├── sp.png                # SabPaisa logo
├── sample_prospect_data.csv # Example CSV for testing
```

## 🚀 How to Use

### 1. Set OpenAI API Key

Create a `.streamlit/secrets.toml` file or use environment variables:

```toml
OPENAI_API_KEY="your-api-key-here"
```

> 💡 Make sure your key has access to `gpt-3.5-turbo`

### 2. Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 3. Or Deploy on Streamlit Cloud

1. Push all files to a GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect the repo and deploy
4. Add your OpenAI key via "Secrets" tab

## 🧪 Sample CSV

Use the included `sample_prospect_data.csv` file to test batch pitch generation.

## 🙏 Credits

Built with ❤️ using:
- [Streamlit](https://streamlit.io)
- [OpenAI Python SDK](https://pypi.org/project/openai/)
