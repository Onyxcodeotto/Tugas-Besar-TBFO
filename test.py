from CYK_ALGORITHM import CYK, CYK_ALT, printFrame
from cfg_parser import cfg_parser, getAllKey
from cfgToCNF import cfgToCnf
from jsparser import read, lexxer, removecomment
from dfa import PreProcess

cfg = cfg_parser("./test_parse_cfg.txt")
cfg = cfgToCnf(cfg)
string = read("input.txt")
string = removecomment(string)

array = lexxer(string)
print(string)
array = PreProcess(array)
#print(array)
frame = CYK_ALT(cfg, array)
benarkah = 'SMain' in frame[0][len(frame)-1]
#print(cfg)
print(array)

printFrame(frame, array)
