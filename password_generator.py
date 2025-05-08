# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:33:34 2024

@author: Madhumitha
"""

import random 
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*@/|\-.?!+$%^#_&"

all=lower+upper+numbers+symbols

len=int(input("HOW MANY CHARACTERS DO YOU WANT TO GENERATE?\n"))
password= "".join(random.sample(all,len))
print("YOUR GENERATED PASSWORD:",password)
