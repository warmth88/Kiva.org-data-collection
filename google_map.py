import csv
import urllib
import json
import time

# use google map to compute the geo location of a lender if possible
def google_map(town):
#    for m in xrange(3):
#        if town[m]==None:
#            town[m]=''
#    request='http://maps.googleapis.com/maps/api/geocode/json?address='+town[0]+',+'+town[1]+',+'+town[2]+'&sensor=false'
    request='http://maps.googleapis.com/maps/api/geocode/json?address='+town+'&sensor=false'
    res=urllib.urlopen(request).read()
    res=urllib.urlopen(request).read()
    res=json.loads(res)
    try:
        lat=res['results'][0]['geometry']['location']['lat']
        lng=res['results'][0]['geometry']['location']['lng']
    except:
        lat=''
        lng=''
    time.sleep(.9)
    return lat,lng

# load file
f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations.csv','r'),delimiter=',')
new=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations_new.csv','w'),delimiter=',')
count=0
total=[]
geo_mapping=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_5.csv','w'),delimiter=',')

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_3.csv','r'),delimiter=',')
exist=[]
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])

geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_4.csv','r'),delimiter=',')
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])
"""
geo_exist=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/geo_mapping_2.csv','r'),delimiter=',')
for i in geo_exist:
    if len(i[1])>5:
        exist.append(i[0])
print len(exist)
print len(set(exist))

"""

print len(exist)
print len(set(exist))

for i in f:
#    if count==100:
#        break
    if len(i[3])==0 and len(i[4])>=5:
        total.append(i[4])
        count+=1
total=set(total)
mapping={}
count=0
g=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations.csv','r'),delimiter=',')

for i in g:
#    if count<1000:
#        continue
    if ((i[4] in total) and (i[4] not in mapping) and len(i[3])==0 and len(i[4])>=5 and (i[4] not in exist)):
        count+=1
        for j in range(len(i[4])):
           if i[4][j].isalpha():
                town=i[4][j:]
                break
        lat,lng=google_map(town)
        mapping[i[4]]=str(lat)+' '+str(lng)
        geo_mapping.writerow([i[4],str(lat)+' '+str(lng)])
        print i
print mapping
print count
print len(total)
print len(set(total))


