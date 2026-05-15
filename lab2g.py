#!/usr/bin/env python3
# Author: Kiera Solomon
# Author ID: ksolomon6
# Date Created: 2026/05/15
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
