import json
import sys

class Notebook():

    def __init__(self, path):

        self.path = path

    def __getitem__(self, item):

        #cell_lst = []
        target_notebook = {}

        with open(self.path) as notebook:

            notebook_str = notebook.read()

            notebook_json = json.loads(notebook_str)

            cells = notebook_json['cells']

        del notebook_json['cells']

        cell_lst = cells[item]

        target_notebook['cells'] = cell_lst

        target_notebook.update(notebook_json)

        return target_notebook

    def __add__(self, other):

        self.other = other

        with open(self.other) as notebook_other:

            notebook_other_str = notebook_other.read()

            notebook_other_json = json.loads(notebook_other_str)

            cells2 = notebook_other_json['cells']

        del notebook_other_json['cells']

        cells1 = cell(self.path)

        target_cells = cells1 + cells2

        target_notebook = {}

        target_notebook['cells'] = target_cells

        target_notebook.update(notebook_other_json)

        target_str = json.dumps(target_notebook)


        target = open('target_notebook.ipynb','w')
        target.write(target_str)

def cell(path):

    with open(path) as notebook:

        notebook_str = notebook.read()

        notebook_json = json.loads(notebook_str)

        cells = notebook_json['cells']

    return cells

