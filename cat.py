import json
import sys
import NB

notebook_path_lst = sys.argv[1:]

notebook = []

target_notebook = {}

cells = []

for path in notebook_path_lst:
    
    notebook.append(NB.Notebook(path))


target_lst = notebook[0]

for nb in notebook[1:]:

    target_lst += nb


with open('target_notebook.ipynb','w') as target:

    target.write(target_lst.jsons())

