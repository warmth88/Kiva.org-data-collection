#!/usr/bin python

f=open('cmd_lender_total.sh','w')
f.write('#!/bin/bash\n')
threads=input('input number of threads')
for i in xrange(int(threads)):
    f.write('python /Users/huanxin/data_fetching/lender_total.py '+str(i)+' '+str(threads)+' &\n')

f.close()
