#!/usr/bin/env python

import sys
from base64 import b64encode, b64decode

if len(sys.argv) != 3:
  print ("Wrong number of arguments")
  print ("Usage:")
  print ('  python encrypt.py X "<somestring>"')
  print ("Where X is a single character")
  exit(1)

key = sys.argv[1]
msg = sys.argv[2]

if len(key) != 1:
  print("Key should just be one character.")
  exit(1)

def encrypt(msg, key):
  output = ""
  for c in msg:
    output += chr(ord(key) ^ ord(c))
  return b64encode(output.encode())

