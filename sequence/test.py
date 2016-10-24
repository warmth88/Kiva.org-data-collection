import csv

f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_sequence.csv','r'),delimiter=',')
count=0
id_list=[]
for i in f:
    if i[3]!='no':
        if i[2] not in id_list:
            id_list.append(i[2])
        count+=1
print count
print len(id_list)
