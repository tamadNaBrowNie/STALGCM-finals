#gets the machine definition from file parses it into a list of tuples that will become state objects
def getMachine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        return parse(stream)
from ast import literal_eval
#parses string to the internal machine definition
def parse(stream):
    lines = stream.splitlines()  
    defs = [literal_eval(strings) for strings in lines]
    return defs


from classes import Machine
from classes import State
def main():
    # put guis stuff here ig
    """ put file path in getMachine args"""
    definitions = getMachine()
    states = [State(state) for state in definitions]
    M = Machine(states)
    #now do fun stuff. dunno if itwill run
    