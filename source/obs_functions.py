from pprint import *
#from intertools import * # to perform with efficient loops
#from networkx import * # to work with  graphics.


def read_my_file(filename):
    try:

        obsidian_artefacts = open(filename)
        # in order to open data that is previously in an accepted format, the variable must be equal to a comand OPEN that will get access to the data

        data = obsidian_artefacts.read()
        # this next part  will be able to read whate is inside my variable "obsidian_artefacts"

        datarows = data.split('\n')


        datarows
        # which will print my information without any speficific  instruction.



        #chop each string in datarows into a list of strings where each splitted string is a cell_value
        cell_values = []
        for eachrow in datarows:
            cell_values.append(eachrow.split(','))


        cell_values
        #print

        obs_dict = {}

        header_keys = cell_values[0]

        for col_index in range(0,len(header_keys)):

            key = header_keys[col_index]

            values=[]

            for row_index in range(1,len(cell_values)-1):
                eachrow = cell_values[row_index]
                values.append(eachrow[col_index])


            obs_dict[key] = values

        return obs_dict


    except FileNotFoundError:
        return None
    except OSError: 
        return None