import json

class Notebook:
    '''
    Read Path, extract cells and meta_data from files
    '''
    
    def __init__(self, path):
        #self.path = path

        self.cells, self.meta_data = self.__read_file(path)

    def __read_file(self, path):

        #return json files

        with open(path) as nb_file:

            s = nb_file.read()

            return self.__read_json(s)

    def __read_json(self, file):
        #read file, return cells and meta_data

        notebook_dct = json.loads(file)

        cells = notebook_dct['cells']

        del notebook_dct['cells']

        return cells, notebook_dct

