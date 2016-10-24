import csv

new=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/final_location_new.csv','w'),delimiter=',')

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations_new.csv','r'),delimiter=',')
exist={}
for i in geo_exist:
    if i[4] not in exist:
        exist[i[4]]=i[3]

f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/supply_list.csv','r'),delimiter=',')
for i in f:
    if i[1] not in exist:
        exist[i[1]]=i[0]


location=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/final_location.csv','r'),delimiter=',')
count=0
for i in location:
    if (len(i[3])==0 and len(i[4])>5 and (i[4] in exist)):
        i[3]=exist[i[4]]
    else:
        if len(i[4])>5:
            count+=1
    new.writerow(i)
print count


