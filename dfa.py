import re

#expfa is non deterministic
#Accept state:q3
class RULE:
    def __init__(self, dict):
        self.transition = dict
    def __getitem__(self ,input):
        for key, val in self.transition.items():
            if(key==input):
                return val
            if(re.match(key, input)):
                return val
        raise KeyError


class NFA:
    def __init__(self,initial, dict, final_state):
        self.start = initial
        self.rule = dict
        self.final = final_state
    def __getitem__(self ,input):
        return self.rule[input]

    def accepts(self, string):
        state = self.start
        banned = ["break", "const", "case", "catch", "continue", "default",
              "delete", "else", "false", "finally", "for", "function",
              "if", "let", "null", "return", "switch", "throw", "try",
              "true", "var","while", " "]
        if string in banned:
            return False
        if string == "":
            return False
        try:
            i=0
            while(i<len(string)):

                state = self[state][string[i]]
                i+=1
            return state == 'q1'
        except KeyError:
            return False
    def add_rule(self,state, rule):#ADD
        self.rule.update({state: rule})
        

def varNFA(string):
    state = 'q0'
    nfa = {'q0': RULE({'[A-Za-z]':'q1'}),
           'q1': RULE({'[A-Za-z0-9_]':'q1'})
           }
    fnfa =  NFA('q0',nfa, ['q0'])

    return fnfa.accepts(string)
 
def intNFA(string):
    final_state = ['q1', 'q2', 'q5']
    state = 'q0'
    nfa = {'q0':RULE({'[0-9]':'q1'}),
            'q1':RULE({'[0-9]':'q1', '.':'q2', 'e':'q3'}),
            'q2':RULE({'[0-9]':'q2', '[eE]':'q3'}),
            'q3':RULE({'[0-9]':'q5', '\+|\-':'q4'}),
            'q4':RULE({'[0-9]':'q5'}),
            'q5':RULE({'[0-9]':'q5'})
            }
    try:
        for i in range(len(string)):
            state= nfa[state][string[i]]
            
        return state in final_state
    except KeyError:
        return False

    
def transformstring(string):
    for i in range(len(string)):
        
        """
def opNFA(array):
    NFA = {'q0':{r'[\+]':'q+', ''
                }
           }"""

operator = []
ifop = ['?']
elseop = [':']
#log op can be and calc op can be excahnged
logical_operator = ['==','>','>=','<','<=','&&', '||','??','===','!==',]
calc_operator = ['+','&', '|','^', '/', '**','<<','*','%','>>','-','>>>']
assign_operator = ['+=', '=', '&=', '|=', '^=','/=', '**=','<<=','&&=', '||=','*=','??=','%=','>>=','-=','>>>=']
prefix_operator = ['!', '~', '+', '-','--','++']
comma = [',']

def classifying_operator(string):
    operator = []
    ifop = ['?']
    elseop = [':']
    #log op can be and calc op can be excahnged
    logical_operator = ['==','>','>=','<','<=','&&', '||','??','===','!==','!=']
    calc_operator = ['+','&', '|','^', '/', '**','<<','*','%','>>','-','>>>']
    assign_operator = ['+=', '=', '&=', '|=', '^=','/=', '**=','<<=','&&=', '||=','*=','??=','%=','>>=','-=','>>>=']
    prefix_operator = ['!', '~', '+', '-','--','++']
    ambigue = ['+','-']
    operator = logical_operator+ifop+elseop+calc_operator+assign_operator+prefix_operator
    result = []
    store = ''
    for i in string:
        
        if store+i in operator:
            store+=i
            continue
        else:
            if (store != ''):
                if i in ambigue:
                    result.append('opAmb')
                else:
                    if store in logical_operator+calc_operator:
                        result.append('opExp')
                    elif store in prefix_operator:
                        result.append('opPrec')
                    elif store in assign_operator:
                        result.append('opAss')
                    elif store in ifop:
                        result.append('opif')
                    elif store in elseop:
                        result.append('opels')
                    
            if i in operator:
                store=i
            else:
                store = ''
                result.append(i)
    return result
            
def transformstring(string):
    ignore = False
    result = []
    stop = ''
    for i in string:
        #Kasus dalam string
        if ignore:
            if(i == stop):
                ignore = False
            continue
        
        # Kasus luar string
        if i == "'" or i == '"':
            stop = i
            ignore = True
        if ignore:
            result.append('benang')
        else:
            result.append(i)
            
    return result
            
            





def PreProcess(array):
    # JANGAN GANTI MENJADI BANNED TERMINAL 
    #F.S.
    #1. Turn all funct,obj,var name as fariabel
    #2. Turn all integer float in any kind of form as angka
    #3. Classificate operator
    #4. Turn all string to setring
    #5. remove whitespase
    banned = ["break", "const", "case", "catch", "continue", "default",
              "delete", "else", "false", "finally", "for", "function",
              "if", "let", "null", "return", "switch", "throw", "try",
              "true", "var","while"]
    temp1 = []
    temp2 = []
    for i in array:
        if varNFA(i):
            temp1.append('variabel')
        else:
            temp1.append(i)
    #2. Transform number
    for i in temp1:
        if intNFA(i):## masih salah
            temp2.append('angka')
        else:
            temp2.append(i)
    
    #3. Class Op
    temp2 = classifying_operator(temp2)
    
    #4. String
    temp2 = transformstring(temp2)
    
    #5. White Space
    while ' ' in temp2:
        temp2.remove(' ')
    while '\n' in temp2:
        temp2.remove('\n')
    return temp2
