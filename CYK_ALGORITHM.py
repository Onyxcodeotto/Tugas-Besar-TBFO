#CYK_ALGORITHM
import itertools
from cfg_parser import getAllKey


def CYK(CNF, input_string):
    # change base later 
    base = [*input_string]
    #empty set
    frame = [[set() for j in input_string] for i in input_string]
    
    for i in range(len(frame)):
        for j in range(0, len(frame)-i):
            if i==0:
                frame[i][j] = getAllKey(CNF, [base[j]])
            else:
                for k in range(i):
                    rule = list(''.join(e) for e in itertools.product(frame[k][j], frame[i-k-1][k+1]))
                    for pair in rule:
                        pair = [*pair]
                        frame[i][j].update(getAllKey(CNF,pair))
    #buat test return frame
    
    return frame
    
def CYK_ALT(CNF, input_string):
    #Pengindexan mengikuti teori, sudah benar
    # Cek apakah S ada di 0, len - 1
    base = [*input_string]
    #empty set
    frame = [[set() for j in input_string] for i in input_string]
    
    for inc in range(0, len(base)):#increment
        for i in range(0, len(base) - inc):#base
            j = i+inc
            if inc==0:
                frame[i][j] = getAllKey(CNF, [base[j]])
            else:
                for k in range(inc):
                    k+=i
                    rule = list(itertools.product(frame[i][k], frame[k+1][j]))
                    for pair in rule:
                        array = [pair[0], pair[1]]
                        frame[i][j].update(getAllKey(CNF,array))
                        
    return frame

def printFrame(frame, base):
    for inc in range(0, len(base)):#increment
        for i in range(0, len(base) - inc):#base
            j = i+inc
            if inc==0:
                print(frame[i][j],end = "   ")
            else:
                print(frame[i][j],end="   ")      
        print("\n")
           
        
            
            