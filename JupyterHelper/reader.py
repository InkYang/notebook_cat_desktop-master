import json

def read_file( path):

    #return json files

    with open(path) as nb_file:

        s = nb_file.read()

        return read_json(s)

def read_json(file):
    #read file, return cells and meta_data

    notebook_dct = json.loads(file)

    cells = notebook_dct['cells']

    del notebook_dct['cells']

    return cells, notebook_dct