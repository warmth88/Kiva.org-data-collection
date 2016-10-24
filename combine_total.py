#!/usr/bin/python
import time
file_num=64 #input('input total file numbers')
prefix='/Users/huanxin/data_fetching/original/'
name1='lenders_total_12052718.csv'
f=open(prefix+name1,'w')

for i in xrange(int(file_num)):
    name='lenders_total_12052718_'+str(i)+'.csv'
    f1=open(prefix+name,'r')
    if i==0:
        for line in f1:
            f.write(line)
    else:
        f1.next()
        for line in f1:
            f.write(line)
    f1.close()
f.close()

