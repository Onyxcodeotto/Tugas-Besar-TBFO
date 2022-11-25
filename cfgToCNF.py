import sys
import itertools
from cfg_parser import notTerminal,getTerminal,containTerminal,getAllKey,getKey, replaceVal

                            
def removeunit(cfg):
    done = False
    delete = []
    add = []
    while not done:
        add = []
        delete = []
        done = True
        for key, val in cfg.items():
            for i in range(len(val)):
                if (len(val[i]) == 1 and notTerminal(val[i])):
                    done = False
                    for j in cfg[val[i][0]]:
                        if j not in val:
                            add.append([key, j])
                        else:
                            continue
                    delete.append([key, val[i]])
        
        for i in add:
            cfg[i[0]].append(i[1])
        for i in delete:
            cfg[i[0]].remove(i[1])
    return cfg
def cfgToCnf(cfg):
    # Asumsi sekarang
    # 1. No useless symbol
    temp = 0
    #Step 1 create new start symbol
    cfg['SMain'] = [['S']]
    
    #Step 2 Simplify
    #a. remove eps (langsung diterapkan)
                
    #b. remove useless symbol (langsung diterapkan)
    #c. remove unit productions print('test')
    
    cfg = removeunit(cfg)
    #step 3 seperate everything with len>2
    newRule = {} 
    for key, val in cfg.items():
        for i in range(len(val)):
            while len(val[i]) > 2:#reverse
                
                head_k = val[i][-2:]
                tail_k = val[i][:-2] 
                keyt = getKey(cfg, [head_k])
                if keyt=='IDX_UNDEF':
                    newRulekey = getKey(newRule, [head_k])
                    if (newRulekey=="IDX_UNDEF"):
                        newkey = 'New_' + str(temp)
                        temp+=1
                        newRule[newkey] =  [head_k]
                        cfg[key][i] = tail_k+[newkey]
                    else:
                        cfg[key][i] = tail_k+[newRulekey]
                else:
                    cfg[key][i] = tail_k + [keyt]
    cfg.update(newRule)
    
    #Step 4 seperate terminals from non terminals
        #cek if len > 1 and contain terminal
    newRule = {}# New rule for next step since we want to update cfg but since we iterating through cfg, we cant change its value
    for i in cfg:
        for j in range(len(cfg[i])):
            if len(cfg[i][j])>1 and containTerminal(cfg[i][j]):
                k = getTerminal(cfg[i][j])
                while(k!='IDX_UNDEF'):
                    key = getKey(cfg, [[k]])
                    if key=='IDX_UNDEF':
                        newRulekey = getKey(newRule, [[k]])
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
    return cfg

