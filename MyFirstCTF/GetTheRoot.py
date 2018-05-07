#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
import numpy.polynomial.polynomial as polynom

r = remote("140.110.112.29", 5122)

r.readline() # ===== Welcome to Get the Root =====
r.readline() # I need you to solve some polynomial for me, just give me one of the roots of the polynomial
r.readline() # ----- wave : example -----
r.readline() # polynomial : 1 -2 1 (which means x^2 - 2x + 1)
r.readline() # root : 1 (just one of the roots, and gurantee to be integer)

# for i in range(0, 100):

r.readline() # ----- wave : 1/100 -----
poly = r.recvuntil("\n").split(" ")[2:]
poly[-1] = poly[-1].strip("\n")
# convert to int
poly = map(int, poly)

result = str(polynom.polyroots(poly)[0])
print polynom.polyroots(poly)
r.sendline(result)
r.interactive()
