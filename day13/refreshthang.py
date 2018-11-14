# __author__ = "TremorAi"
# import requests
# host = "http://ctf.slothparadise.com/about.php"

# for i in range(100):
#     requests.get(host)
#     print(i)
import sys
from base64 import b64encode, b64decode
from string import printable
msg = "bWN/XXVDRVRDUmVJQkNVcU9STn5JVFVnVENIAVJwQ1RfdUNFVENSWw=="
dict1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","e","s","t","u","v","w","x","y","z"]
#b'm
output = ""

def encrypt(msg, key):
  output = ""
  for c in msg:
    output += chr(ord(key) ^ ord(c))
  return b64encode(output.encode())

# for x in dict1:
#     for c in msg:
#         output += chr(ord(x) ^ ord(c))
#         print(output)
#     output = ""
for x in printable:        
    enc = encrypt(b64decode(msg).decode(), "&")
    print(b64decode(enc).decode())
    