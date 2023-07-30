def getMachine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        return stream
def doString(string, machine):
    i = 0
    while i < len(string) or flag:
        if i  < 0:
            return False
        input = string[i]
        flag= machine.read_char(input)
        if flag != 1 or flag != 0 or flag != -1:
            return False
        