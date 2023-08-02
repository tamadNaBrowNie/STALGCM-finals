
"""this is the machine give it a list of State objects. the element is always the start state

    members:
        list: states is a list of State objects
        run: is the current state. the first state is always the first object in states
        
"""

class Machine:
    def __init__(self, states):
        self.states = states
        self.run = self.states[0]
        """this function lets machine read the character. 
        returns: a tuple of (new current state, read direction)
        """
    def read_char(self,char):
        delta = self.run.get_delta(char)
        self.run = next(state for state in self.states if delta[0] == state.label)
        return (self.run,delta[1])
        """returns if current state is a final state.
        """
    def isFinal(self):
        return self.run.isFinal

        """This class simulates a state in a machine

        members:
            string: label is the label of state
            list: delta contains a list of tuples that represent the transitions
            boolean: isFinal dictates if it is a final state
        notes:
            the list members are of the following types:
                (string_literal, Number,string_literal)
                they stand for (next state label, direction of read (-1 for left, 0 for stay, 1 for right), the character to read)
        """
class State:
    def __init__(self,state):
        self.label, self.delta, self.isFinal = state
        """find a valid transition given character
        """
    def get_delta(self,char):
        return next(val for val in self.delta if val[2] == char)

