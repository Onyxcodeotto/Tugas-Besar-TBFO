#CYK_ALGORITHM

import cfg_parser


def CYK(CNF, input_string):
    base = input_string.split()
    #empty set
    frame = [[{} for j in input_string] for i in input_string]
    for i in range(len(frame)):
        for j in range(0, len(frame)-i):
            if i==0:
                frame[i][j] = getAllKey(CNF, [base[0]])
            else:
                #X i j = (Xii*X(i-1)j) Union (XI,I-1) (XI+2,J)
                