#!/usr/local/opt/python/bin/python3.7

# Version: 20190804-2145
# test distribution of random.choice() w/out setting seed value.

import random 

n = ["red", "orange", "yellow", "green", "blue", "violet", "black", "white"]
c = [0,0,0,0,0,0,0,0]

for x in range(0,500): 
	p = random.choice(n) 
	for y in range(0,7):
		if (n[y] == p): 
			c[y] += 1
			break
	
for x in range(0,7): 
	print(c[x])

