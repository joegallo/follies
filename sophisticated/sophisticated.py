#!/usr/bin/env python

import base64
import string
import sys

# base32 because index names must be lowercase
def string_encode(s):
    return base64.b32encode(s).lower()

def string_decode(s):
    return base64.b32decode(s, casefold=True)

def string_chunk(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def doc_encode(id, s):
    e = string_encode(s)
    chunks = string_chunk(string_encode(s), 64)
    l = len(str(len(chunks))) # num chars for the index counter
    icf = '{:0'+str(l)+'d}' # index counter formatter
    return ["{}_{}_{}".format(id, icf.format(i), c.replace('=','_')) for i, c in enumerate(chunks)]

def doc_decode(lines):
    l = [line.split('_',2)[2].strip() for line in lines]
    s = string.join(l, '').replace('_','=')
    return string_decode(s.strip())

if __name__ == "__main__":
    operation = 'encode'

    if (len(sys.argv) == 2 and sys.argv[1] == "-d"):
        operation = 'decode'

    if operation == 'encode':
        id = sys.argv[2]
        s = sys.stdin.read().strip()
        names = doc_encode(id, s)
        for name in names:
            print name

    if operation == 'decode':
        s = sys.stdin.readlines()
        print doc_decode(s)
