#this is the machine give it a list of State objects. the element is always the start state
#

class Machine:
    def __init__(self, states):
        self.states = states
        self.run = states[0]
        #machine reads char. returns tuple of direction and isfinal
    def read_char(self,char):
        delta = self.run.get_delta(char)
        self.run = next(state for state in self.states if delta[0] == state.label)
        return (self.isFinal(),delta[1])
    def isFinal(self):
        return self.run.accept()
#this is a state in the machine. it should accept a tuple of (string, list, boolean)
#its members are (label, deltas, finalstate?)
#the second member is a list of tuples of (string, integer[-1,0,1], string). 
# the members are (next state, direction,what to read)
class State:
    def __init__(self,state):
        self.label, self.delta, self.isFinal = state
    def get_delta(self,char):
        return next(val for val in self.delta if self.delta[2] == char)
    def accept(self):
        return self.isFinal()
from ast import literal_eval
#this class parses the definition. initiate it with the stream of the file
class MDParser:
        stream = ""
        lines = []
        defs= []
        def __init__(self,stream):  
            self.stream = stream
            self.parse()
        def parse(self):
            lines = self.stream.splitlines()  
            self.lines = [literal_eval(strings) for strings in lines]
            self.defs = [(elem[0],literal_eval(elem[1]),elem[2]) for elem in lines]

def getStates(list_of_states):
    states = [State(state) for state in list_of_states]
    return states
