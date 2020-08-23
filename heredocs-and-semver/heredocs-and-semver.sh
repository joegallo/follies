#!/bin/bash

read -r -d '' CMD << '--END'

import sys
from distutils.version import LooseVersion

for line in sys.stdin.readlines():
    v = LooseVersion(line.split(' ')[0])
    if v.version[1] % 2 == 0 or v.version[2] % 2 == 0:
       print line

--END

# imagine this is just one tiny part of an otherwise reasonable amount
# of bash
python -c "$CMD" < $1
