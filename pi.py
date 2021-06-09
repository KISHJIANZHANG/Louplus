# pi.py
from random import random
from math import sqrt

DARTS = pow(2,25)
hits=0

for i in range(1,DARTS):
    x , y = random() , random()
    dist=sqrt(x**2+y**2)
    if dist <=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
print('The value of pi si %s' % pi)
