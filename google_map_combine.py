import csv

new=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/final_locations_new.csv','w'),delimiter=',')

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_3.csv','r'),delimiter=',')
exist=[]
mapping={}
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])
        mapping[i[0]]=i[1]

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_4.csv','r'),delimiter=',')
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])
        mapping[i[0]]=i[1]

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_5.csv','r'),delimiter=',')
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])
        mapping[i[0]]=i[1]


print len(exist)
print len(set(exist))

location=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations.csv','r'),delimiter=',')
count=0
for i in location:
    if (len(i[3])==0 and len(i[4])>5 and (i[4] in mapping)):
        i[3]=mapping[i[4]]
        count+=1
    new.writerow(i)
print count


