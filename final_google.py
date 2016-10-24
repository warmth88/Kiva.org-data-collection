import csv
import urllib
import json
import time

def google_map(town):
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


g=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/supply_list.csv','w'),delimiter=',')
f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/miss_list.csv','r'),delimiter=',')
count=0
for i in f:
#    if count==3:
#        break
    count+=1
    lat,lng=google_map(i[0])
    if lat=='' and lng=='':
        g.writerow(['',i[0]])
    else:
        g.writerow([str(lat)+' '+str(lng),i[0]])
    print [str(lat)+' '+str(lng),i[0]]
    print count




