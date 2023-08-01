#gets the machine definition from file
def getMachine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        return stream
#machine reads string. do not use. implement this in driver instead
def doString(string, machine):
    i = 0
    final = False
    while i < len(string) or not final :
        if i  < 0:
            return False
        input = string[i]
        flag= machine.read_char(input)
        if flag != 1 or flag != 0 or flag != -1:
            return False
        final = machine.run.isFinal
        i+=flag
    return True
        