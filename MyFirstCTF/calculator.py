#! /usr/bin/python
# -*- coding: utf-8 -*-
from pwn import *

context.log_level = "DEBUG"

host = "140.110.112.29"
port = 5119

r = remote(host, port)

r.readline() # ===== Welcome to the magic calculator =====
r.readline() # We got some equations here, but the operator is missing.
r.readline() # Can you help us?

for i in range(1,101):
    r.readline() # ----- wave 1/100 -----
    Formula = r.readline()
    # 開始分別抓取元素 (Formula是字串型態，加上 int 轉成數字型態)
    First_element = int(Formula.split(' ')[0])
    Second_element = int(Formula.split(' ')[2])
    Result = int(Formula.split(' ')[4])
    # 開始進行比對，並且找出正確的運算子
    if First_element + Second_element == Result:
        r.sendline("+")
    elif First_element - Second_element == Result:
        r.sendline("-")
    elif First_element * Second_element == Result:
        r.sendline("*")

r.interactive()

