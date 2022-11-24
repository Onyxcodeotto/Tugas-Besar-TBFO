import sys
import itertools
from cfg_parser import notTerminal

def removeunit(cfg):
    emptyArray = []
    for key, val in cfg.items():
        for i in range(len(val)):
            if (len(val[i]) == 1 and notTerminal(val[i])):
                for j in cfg[val[i][0]]:
                    if i not in val[i]:
                        val.append(j)
                    else:
                        continue
                emptyArray.append([key, val[i]])
    for i in emptyArray:
        print(cfg[i[0]])
        print(i[1])
        cfg[i[0]].remove(i[1])
    return cfg
