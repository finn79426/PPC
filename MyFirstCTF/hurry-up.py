#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
import time

def caeser_cipher(string, offset, plaintext):
    for j in string:
        if ord(j) not in range(ord("A"), ord("Z")+1): # If j not in 65~90, I can confirm it's NOT an alphabet
            plaintext += j 
        else:
            if (ord(j) + offset) < 65: # if (j - offset) less then "A", we need to plus that to "Z", so it can continue.
                plaintext += chr((ord(j) + offset) + 26)
            elif (ord(j) + offset) > 90: # Reversing previous step.
                plaintext += chr((ord(j) + offset) - 26)
            else:
                plaintext += chr(ord(j) + offset) # No problem mean ALL GOOD. :p
    print "Plaintext is : ", plaintext
    return plaintext
 



r = remote("140.110.112.29", 5123)
context.log_level = "DEBUG"

r.readline() # Hurry up, winter is coming...
r.readline() # ===== wave 1/100 =====   

for i in range(0, 100):
    raw_string = r.recvuntil(": ") # shift every alphabet in the word by ?? : 
    offset = int(raw_string.split(" ")[-3])
    string = r.recvuntil("\n")
    plaintext = ""  

    print "======================="
    print "Offset is : ", offset
    print "Raw String is : ", string
    print "======================="

    r.send(caeser_cipher(string, offset, plaintext))
    r.readline()
r.interactive()

