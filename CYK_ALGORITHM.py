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
                    print(frame[j][k])
                    print(frame[k][i])
                    print(rule)
                    for pair in rule:
                        pair = [*pair]
                        print(pair)
                        frame[i][j].update(getAllKey(CNF,pair))
    #buat test return frame
    
    return frame
                