#!/usr/bin/python
import time
file_num=64 #input('input total file numbers')
prefix='/Users/huanxin/data_fetching/data/'
if int(time.strftime('%H'))==9:
    name1='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+'0'+str(int(time.strftime('%H'))-1)+'.csv'
else:
    name1='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+str(int(time.strftime('%H'))-1)+'.csv'
f=open(prefix+name1,'w')

for i in xrange(int(file_num)):
    if int(time.strftime('%H'))==9:
        name='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+'0'+str(int(time.strftime('%H'))-1)+'_'+str(i)+'.csv'
    else:
        name='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+str(int(time.strftime('%H'))-1)+'_'+str(i)+'.csv'
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

