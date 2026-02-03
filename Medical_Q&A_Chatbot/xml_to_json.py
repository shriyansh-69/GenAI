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

        try :
            tree = et.parse(file_path)
            root = tree.getroot()

            qapairs = root.find("QAPairs")
            if qapairs is None:
                continue

            for qa in qapairs.findall("QAPair"):
                q = qa.find("Question")
                a = qa.find("Answer")

            if q is None or a is None:
                continue


            question = q.text.strip()
            answer = a.text.strip()

            all_qa.append({
                "question" : question,
                "answer" : answer
            })

        except Exception as e:
            print(f"Skipped {file_path} بسبب error: {e}")



            







        