# open file for read
#import os
import csv
import os

"""
file_list=os.listdir('/Users/wuhuanxin/data_fetching/missing_final/')
ID_list=[]
for i in file_list:
    file_open=csv.reader(open('/Users/wuhuanxin/data_fetching/missing_final/'+i,'r'),delimiter=',')
    for j in file_open:
        if j[1] in ID_list:
            pass
        else:
            ID_list.append(j[1])
    ID_list=ID_list[1:]
    ID_cache=csv.writer(open('/Users/wuhuanxin/data_fetching/missing_final/IDs.csv','w'),delimiter=',')
    ID_cache.writerow(ID_list)
    print i
print len(file_list)
print len(ID_list)

"""
ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/missing_final/IDs.csv','r'),delimiter=',')
for i in ID_cache:
    print len(i)
    break
print i

ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/original/all_loans.csv','r'),delimiter=',')
ID_list=[]
for j in ID_cache:
    ID_list.append(j[0])
print len(set(ID_list))
ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/original/missing_loans.csv','r'),delimiter=',')
for j in ID_cache:
    ID_list.append(j[0])
print len(ID_list)
ID=set(i).difference(set(ID_list))

print len(ID)
ID=list(ID)

f=csv.writer(open('/Users/wuhuanxin/data_fetching/missing_final/missing_IDs.csv','w'),delimiter=',')
initial=['borrower_id']
f.writerow(initial)
for i in ID:
    f.writerow([i])

