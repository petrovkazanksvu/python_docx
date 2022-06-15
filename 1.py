from os import chdir
from docx import Document
import os
chdir("/home/geo/tasks/python_jobs")
doc= Document("/home/geo/tasks/python_jobs/my_word_file.docx")
all_paras = doc.paragraphs
for para in all_paras:
    print(para.text)
    print("-------")
