#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np
whole=[]
counter=0
length=[]
for i in os.listdir('./original'):
    if i[0:7]=='lenders':
        f=csv.reader(open('./original/'+i,'r'),delimiter=',')
        for j in f:
            whole.append(j[0])
        whole=list(set(whole))
        length.append(len(whole))
        counter+=1
x=np.arange(counter)
width=0.35
fig=plt.figure()
print length
print x
plt.bar(x,length,width)
plt.ylabel('total number of active users')
plt.xlabel('data collection series')
fig.savefig('growth.jpg')
plt.show()


