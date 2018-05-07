#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

r = remote("140.110.112.29", 5127)
context.log_level = "DEBUG"

r.readline() # ===== Welcome =====
r.readline() # I need you to transform from Fahrenheit to Celsius
r.readline() # ----- wave : example -----
r.readline() # Fahrenheit : 10 (guarantee to be integer)
r.readline() # Celsius : -110/9

for i in range(0, 100):

    r.recvuntil("\n") # ----- wave : 1/100 -----
    F = int(r.recvuntil("\n").split(" ")[2].strip("\n"))
    C = (F-32) * 5
    send = str(C) + "/9"
    r.sendline(send)

r.interactive()
