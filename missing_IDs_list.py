import csv


ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/missing/IDs.csv','r'),delimiter=',')
for i in ID_cache:
    print len(i)
    break


ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/original/all_loans.csv','r'),delimiter=',')
ID_list=[]
for j in ID_cache:
    ID_list.append(j[0])
print len(ID_list)
ID=set(i).difference(set(ID_list))

print len(ID)
ID=list(ID)

f=csv.writer(open('/Users/wuhuanxin/data_fetching/missing/missing_IDs.csv','w'),delimiter=',')
initial=['borrower_id']
f.writerow(initial)
for i in ID:
    f.writerow([i])


