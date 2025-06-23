import pandas as pd
import xml.etree.ElementTree as ET

def generate_xml_report():
    try:
        df = pd.read_csv("prospects_with_pitch.csv")
    except FileNotFoundError:
        return None

    root = ET.Element("Prospects")
    for _, row in df.iterrows():
        item = ET.SubElement(root, "Prospect")
        for col in df.columns:
            child = ET.SubElement(item, col)
            child.text = str(row[col])
    tree = ET.ElementTree(root)
    output_path = "smipe_report.xml"
    tree.write(output_path)
    return output_path
