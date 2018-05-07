#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

context.log_level = "DEBUG"

f0 = lambda x: (3*(x**2)) + x + 3
f1 = lambda x: (5*(x**2)) + 8
f2 = lambda x: (4*(x**3)) + (6*x) + 6
f3 = lambda x: (7*(x**3)) + (5*(x**2))
f4 = lambda x: (x**2) + 4*x + 3


r = remote("140.110.112.29", 5124)
r.recvuntil("f(x) = 28\n")



for i in range(0, 100):
    r.readline()
    mode = r.recvuntil("\n").split()[-1]
    x = int(r.recvuntil("\n").split()[-1])
    print "Mode: ",  mode
    print "x: ", x

    if mode == "0":
        r.sendline(str(f0(x)))
    elif mode == "1":
        r.sendline(str(f1(x)))
    elif mode == "2":
        r.sendline(str(f2(x)))
    elif mode == "3":
        r.sendline(str(f3(x)))
    else:
        r.sendline(str(f4(x)))



r.interactive()


