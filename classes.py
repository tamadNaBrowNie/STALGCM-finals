class Machine:
    def __init__(self, states):
        self.states = states
        self.run = states[0]
    def read_char(self,char):
        delta = self.run.get_delta(char)
        self.run = next(state for state in self.states if delta[0] == state.label)
        return delta[1]
    def isFinal(self):
        return self.run.accept()
class State:
    def __init__(self,state):
        self.label, self.delta, self.isFinal = state
    def get_delta(self,char):
        return next(val for val in self.delta if self.delta[2] == char)
    def accept(self):
        return self.isFinal()
from ast import literal_eval
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
def getDefinition(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        return stream
def getStates(list_of_states):
    states = [State(state) for state in list_of_states]
    return states
def getMachine(states):
    machine = Machine(states)
    return machine
        