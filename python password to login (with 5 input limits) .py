import os
import sys
import time

password = 1399
passinlim = 5
passincount = 0

while passincount < passinlim:
    passin = int(input("Please enter the password: "))
    passincount += 1
    if passin == password:
        print ("Welcome!")
    break
