#!/usr/bin/python3.11
import os
os.system('clear')



factor = int(input("factor from: "))
for i in range(1, factor + 1):
    if factor % i == 0: # menggunakan sisa bagi
        print(i)
    else: 
        continue 


