from CYK_ALGORITHM import CYK, CYK_ALT
from cfg_parser import cfg_parser, getAllKey


cfg = cfg_parser("./test_parse_cfg.txt")

print(cfg)
# lets try cut space method
frame = CYK_ALT(cfg, "baaab")
benarkah = 'S' in frame[0][4]


print(frame)
print(benarkah)
