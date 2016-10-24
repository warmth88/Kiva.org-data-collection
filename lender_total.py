#! usr/bin python

import urllib
import csv
import json
import time
from lender import *
import sys
import os

lender_ID=''
prefix='/Users/huanxin/data_fetching/original/'
name='lenders_total_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'_'+str(sys.argv[1])+'.csv'

lender_main=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['LenderID','Location','MemberSince','HowManyLoans','HowManyTeam','HowManyInvites','Portfolio_Female','AverageGDP','Middle East','Asia','Africa','Eastern Europe','South America','Central America','North America']
lender_main.writerow(initial)

IDs=[]
# scanning all the whole list of lenders.
for i in os.listdir('/Users/huanxin/data_fetching/original'):
    if i[0:7]=='lenders':
        f=csv.reader(open('/Users/huanxin/data_fetching/original/'+i,'r'),delimiter=',')
        for j in f:
            IDs.append(j[0])
        IDs=list(set(IDs))

name='error_total_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.txt'
f=open(prefix+name,'a')

for i in xrange(len(IDs)):
    if i%int(sys.argv[2])==int(sys.argv[1]):
        try:
            lender_main.writerow(lenders(IDs[i]))
        except:
            f.write(IDs[i])
            f.write('\n')
    if (i-int(sys.argv[1]))%64==0:
            print round(float(i)/len(IDs)*100,2),len(IDs),sys.argv[1]

f.close()
print 'done successfully!'





