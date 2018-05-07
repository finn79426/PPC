#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
import time

r = remote("140.110.112.29", 5123)
context.log_level = "DEBUG"

r.readline() # Hurry up, winter is coming...
r.readline() # ===== wave 1/100 =====

for i in range(0, 100):
    raw_string = r.recvuntil(": ") # shift every alphabet in the word by ?? : 
    offset = int(raw_string.split(" ")[-3])
    string = r.recvuntil("\n")

    print "======================="
    print "Offset is : ", offset
    print "Raw String is : ", string
    print "======================="

    plaintext = ""  
    for j in string:
        if ord(j) not in range(ord("A"), ord("Z")+1):
            plaintext += j
        else:
            if (ord(j) + offset) < 65:
                plaintext += chr((ord(j) + offset) + 26)
            elif (ord(j) + offset) > 90:
                plaintext += chr((ord(j) + offset) - 26)
            else:
                plaintext += chr(ord(j) + offset)
    print "Plaintext is : ", plaintext
    r.send(plaintext)
    # sleep(0.1)
    r.readline()
    # sleep(0.1)
r.interactive()

