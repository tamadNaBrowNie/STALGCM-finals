class Machine:
    def __init__(self, states):
        self.states = states
        self.run = states[0]
    def read_char(self,char):
        delta = self.run.get_T
        self.run = [state for state in self.states if delta[0] == state.label]
        if(delta[1] == 'L'):
            return -1
        elif (delta[1] == 'R'):
            return 1
        else:
            #TODO: add errorhandling here
            pass
class State:
    def __init__(self,label,delta):
        self.label = label
        self.delta = delta
    def get_T(self,char):
        return [val for val in self.delta if char == val[2]]
from ast import literal_eval
class MDParser:
        stream = ""
        lines = []
        defs= []
        def __init__(self,stream):  
            self.stream = stream
        def parse(self):
            lines = self.stream.splitlines()  
            self.lines = [literal_eval(strings) for strings in lines]
            self.defs = [(elem[0],literal_eval(elem[1]),elem[2]) for elem in lines]
def getMachine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        return stream
        
        