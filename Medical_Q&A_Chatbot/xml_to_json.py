import xml.etree.ElementTree as et
import json 
import os


xml_root = "data/xml/MedQuAD"
output_root = "data/medquad.json"

all_qa = []

for root_dir, _, files in os.walk(xml_root):
    for file  in files:
        if not files.endswith(".xml"):
            continue

        file_path = os.path.join(root_dir,files)

        


        