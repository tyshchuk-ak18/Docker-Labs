import docx

doc = docx.Document("lab.docx")
all_paras = doc.paragraphs
for para in all_paras:
    print(para.text)
    print("-------")
