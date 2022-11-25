import re


def cfg_parser(path):
    cfg = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            if line[0] == "#" or line[0] == '\n':
                continue
            
            parts = line.split('->')
            parts[1] = parts[1].strip('\n')
            parts[0] = parts[0].strip()
            parts[1] = parts[1].strip()
            """
            ALTERNATE PARSING
            We need
            """
            parts[1] = re.sub(' +',' ',parts[1])# replace multiple space to single space
            if parts[0] not in cfg.keys():
                parts[1] = parts[1].split('|')
                cfg[parts[0]] = [re.sub(' +', ' ', i.strip()).split(' ') for i in parts[1]]
            else:
                cfg[parts[0]] = cfg[parts[0]] + [parts[1].split()]
    f.close()
    return cfg
    
    
def getTerminal(array):
    #return first terminal
    for i in array:
        if isTerminal(i):
            return i
    return 'IDX_UNDEF'
def isTerminal(string):
    return not notTerminal(string)

def notTerminal(string):
    return string[0].isupper()

def getKey(dictionary, value):#return first keu
    for key, val in dictionary.items():
        if value == val:
            return key 
    return 'IDX_UNDEF'

def getAllKey(dictionary, value):
    # val format:  ['val']
    #return empty set if none
    temp = set()
    for key,val in dictionary.items():
        for j in val:
            
            if value == j: 
                
                
                temp.update([key])
    return temp

def containTerminal(array):
    Terminal = False
    for i in array:
        if isTerminal(i):
            Terminal = True
            break
    return Terminal

def replaceVal(array, valfrom, valinto):
    for i in range(len(array)):
        if array[i] == valfrom:
            array[i] = valinto
    return array

def isMixed(array):
    terminal = False
    nonTerminal = False
    i=0
    while ((i<len(array)) &  ~( terminal | nonTerminal)):
        if isTerminal(i):
            terminal = True
        if notTerminal(i):
            nonTerminal = True
        i+=1
    return (terminal & nonTerminal)