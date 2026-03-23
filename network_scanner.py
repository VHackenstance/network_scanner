#!usr/bin/env python
from helpers.utils import scan, check_for_root

check_for_root()
scan("192.168.1.254/24")