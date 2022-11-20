from CYK_ALGORITHM import CYK
from cfg_parser import cfg_parser, getAllKey


cfg = cfg_parser("./test_parse_cfg.txt")


# lets try cut space method
frame = CYK(cfg, "ababa")

