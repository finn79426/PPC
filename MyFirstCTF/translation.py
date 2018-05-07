#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
from libnum import n2s, s2n

context.log_level = "DEBUG"
r = remote("140.110.112.29", 5125)

r.readline() # ========== Welcome ==========
r.readline() # I give you a string, you need to translate it to integer in big endian
r.readline() # ----- wave : example -----
r.readline() # string : ab (all the string will contain lowercase alphabets only)
r.readline() # integer : 24930 ( which comes from 97 * 256 + 98 = 24930 )

for i in range(0, 100):

	r.readline()

	string = r.recvuntil("\n").split(" ")[2].strip("\n")
	string_len = len(string) - 1
	number = 0

	print "====================="
	print "String = ", string
	print "pow = ", string_len
	print "====================="

	for j in string:
            j = s2n(j)
            number += j * 256 ** string_len
    	    string_len -= 1
    
	print "Result = ", number

	r.recvuntil("integer : ")
	r.sendline(str(number))
    
r.interactive()
