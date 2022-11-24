#cfgParser


#
import re


def cfg_parser(path):
    cfg = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            
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


def cfgToCnf(cfg):
    # Asumsi sekarang
    # 1. No epsilon
    # 2. CFG is already simplified
    # Masalah
    # 1. Belum bisa handle non terminal dengan length 1
    temp = 0
    #Step 1 create new start symbol
    cfg['SMain'] = [['S']]
    
    #Step 2 Simplify
    #a. remove eps (nanti)
    #for i in cfg:
       # for j in cfg[i]:
       #     if 'eps' in j:# find epsilon
       #         print(i)
                
    #b. remove useless symbol (langsung diterapkan di docs)
    #c. remove productions (langsung diterapkan di docs)
    
    #Step 3 seperate terminals from non terminals
    notDone = True
    """ while notDone:
        # Cek whether is its still mixed
        notDone = False
        for i in cfg:
            for j in cfg[i]:
                if isMixed(j):
                    notDone = True
        
        if(not(notDone)):
            break
    """
    #cek if len > 1 and contain terminal
    newRule = {}# New rule for next step since we want to update cfg but since we iterating through cfg, we cant change its value
    for i in cfg:
        for j in range(len(cfg[i])):
            if len(cfg[i][j])>1 &containTerminal(cfg[i][j]):
            
                k = getTerminal(cfg[i][j])
                while(k!='IDX_UNDEF'):
                    key = getKey(cfg, [k])
                    if key=='IDX_UNDEF':
                        newRulekey = getKey(newRule, [k])
                        if (newRulekey=="IDX_UNDEF"):
                            newkey = 'New_' + str(temp)
                            temp+=1
                            newRule[newkey] =  [[k]]
                            cfg[i][j] = replaceVal(cfg[i][j],k,newkey)
                        else:
                            cfg[i][j] = replaceVal(cfg[i][j], k, newRulekey)
                    else:
                        
                        cfg[i][j] = replaceVal(cfg[i][j], k, key)

                    k = getTerminal(cfg[i][j])
                    # change all terminal into non terminal
    
    #append newRule
    cfg.update(newRule)
    #step 4 seperate non terminals with len>2
    newRule = {}    
    for i in cfg:
        for j in range(len(cfg[i])):
            while(len(cfg[i][j])>2):
            #if len>2
                k = cfg[i][j][:2]
                tail_k = cfg[i][j][2:]
                key = getKey(cfg, [k])
                if key=='IDX_UNDEF':
                    newRulekey = getKey(newRule, [k])
                    if (newRulekey=="IDX_UNDEF"):
                        newkey = 'New_' + str(temp)
                        temp+=1
                        newRule[newkey] =  [k]
                        cfg[i][j] = [newkey]+tail_k
                    else:
                        cfg[i][j] = [newRulekey]+tail_k
                else:
                    cfg[i][j] = [key]+k
    cfg.update(newRule)
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
            array[i]= valinto
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
    
    """

cfg = cfg_parser('test_parse_cfg.txt')

print(cfg)
cnf = cfgToCnf(cfg)
print(getAllKey(cfg,['A', 'S']))

print(cnf)"""