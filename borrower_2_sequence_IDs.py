from lending_sequence import *
import csv
import os
#ip_name,ip_address,seq=sequence(436342)

# open file for read
file_list=os.listdir('/Users/huanxin/data_fetching/sequence')
ID_list=[]
for i in file_list:
    file_open=csv.reader(open('/Users/huanxin/data_fetching/sequence/'+i,'r'),delimiter=',')
    for j in file_open:
        if j[0] in ID_list:
            pass
        else:
            ID_list.append(j[0])
    ID_list=ID_list[1:]
    ID_cache=csv.writer(open('/Users/huanxin/data_fetching/sequence/IDs.csv','w'),delimiter=',')
    ID_cache.writerow(ID_list)
print len(file_list)
print len(ID_list)

#for j in ID_list:
#    ip_name,ip_address,seq=sequence(j)


