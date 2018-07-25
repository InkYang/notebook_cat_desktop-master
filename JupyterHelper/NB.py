import json
from . import reader

class Notebook:
    '''
    Read Path, extract cells and meta_data from files
    '''
    
    def __init__(self, path=None):
        #self.path = path
        if path is not None:
    
            self.cells, self.meta_data = reader.read_file(path)

    def __read_file(self, path):

        #return json files

        with open(path) as nb_file:

            s = nb_file.read()

            return reader.read_json(s)

    def __read_json(self, file):
        #read file, return cells and meta_data

        notebook_dct = json.loads(file)

        cells = notebook_dct['cells']

        del notebook_dct['cells']

        return cells, notebook_dct

    def __add__(self, anther):

        # nb1 + nb2

        cells = self.cells + anther.cells

        notebook = Notebook()

        notebook.cells = cells

        notebook.meta_data = self.meta_data

        return notebook

    def jsons(self):

        dct = {'cells':self.cells}

        dct.update(self.meta_data)

        return json.dumps(dct, indent=4)


