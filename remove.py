#!/usr/bin/python

import os
import time
for i in xrange(64):
    if int(time.strftime('%H'))==9:
        name='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+'0'+str(int(time.strftime('%H'))-1)+'_'+str(i)+'.csv'
    else:
        name='lenders_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+str(int(time.strftime('%H'))-1)+'_'+str(i)+'.csv'
    cmd='rm /Users/huanxin/data_fetching/data/'+name
    os.system(cmd)

#name='error_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.csv'
#try:
#    cmd='rm /Users/huanxin/data_fetching/data/'+name
#except:
#    pass
