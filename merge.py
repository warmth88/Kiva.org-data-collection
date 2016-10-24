import csv
import os

file_list=os.listdir('/Users/wuhuanxin/data_fetching/merge/')

file_new=csv.writer(open('/Users/wuhuanxin/data_fetching/lenders.csv','w'),delimiter=',')
count=0
for i in file_list:
    file_open=csv.reader(open('/Users/wuhuanxin/data_fetching/merge/'+i,'r'),delimiter=',')
    for k in xrange(len(i)):
        if i[k:k+2]!='s_':
            pass
        else:
            break
    timestamp=i[k+2:k+10]
    print timestamp
    if count!=0:
        file_open.next()
        for j in file_open:
            j.insert(0,timestamp)
            file_new.writerow(j)
    else:
        for j in file_open:
            j.insert(0,timestamp)
            file_new.writerow(j)
    count+=1
    print count


