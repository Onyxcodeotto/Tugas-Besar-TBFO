

#expfa is non deterministic
#Accept state:q3


def varNFA(string):
    state = 'q0'
    NFA = {'q0':{r'[A-Za-z]':'q1'},
           'q1':{r'[A-Za-z0-9_]':'q1'}
           }
    try:
        if string == "":
            return False
        i=0
        while(i<len(string)):
            state = NFA[state][string[0]]
        return True
    except KeyError:
        return False
        
#def opNFA(array):
    #NFA = {'q0':{r'[\+]':'q+', ''
     #            }
      #     }

operator = ['*', '=', ':', '']

def applyFA(array):
    banned = ["break", "const", "case", "catch", "continue", "default",
              "delete", "else", "false", "finally", "for", "function",
              "if", "let", "null", "return", "switch", "throw", "try",
              "true", "var","while"]
    for i,terminal in enumerate(array):
        
        
        
        if terminal in banned:
            continue
        
print(varNFA(''))        
            
                    

    