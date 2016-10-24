import csv

g=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/lending_sequence_final.csv','w'),delimiter=',')
f1=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_sequence.csv','r'),delimiter=',')
f2=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/final_order.csv','r'),delimiter=',')

for i in f1:
    g.writerow(i)

count=0
for i in f2:
    if count==0:
        print 'pass'
        count+=1
        continue
    g.writerow(i)

