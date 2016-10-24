import csv

f=csv.reader(open('/Users/wuhuanxin/data_fetching/lenders.csv','r'),delimiter=',')
f_new=csv.writer(open('/Users/wuhuanxin/data_fetching/lenders_shrink.csv','w'),delimiter=',')

for i in f:
    f_new.writerow(i[0:16])
