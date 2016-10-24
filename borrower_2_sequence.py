from lending_sequence import *
import csv
import os
import urllib
import json
import time

# use google map to compute the geo location of a lender if possible
def google_map(town):
    for m in xrange(3):
        if town[m]==None:
            town[m]=''
    request='http://maps.googleapis.com/maps/api/geocode/json?address='+town[0]+',+'+town[1]+',+'+town[2]+'&sensor=false'
    res=urllib.urlopen(request).read()
    res=json.loads(res)
    try:
        lat=res['results'][0]['geometry']['location']['lat']
        lng=res['results'][0]['geometry']['location']['lng']
    except:
        lat=''
        lng=''
    time.sleep(.5)
    return lat,lng

# open IDs list
IDs=csv.reader(open('/Users/huanxin/data_fetching/sequence/IDs.csv','r'),delimiter=',')
location=csv.writer(open('/Users/huanxin/data_fetching/sequence/lending_locations.csv','w'),delimiter=',')
location.writerow(['Borrower_ID','Lender_final_count','LenderID_ordered_by_lending','Lender_Geo_Location','Lender_HomeTown'])
order=csv.writer(open('/Users/huanxin/data_fetching/sequence/lending_sequence.csv','w'),delimiter=',')
order.writerow(['Borrower_ID','Lender_final_count','LenderID_ordered_by_lending','Is_Fellow'])
error=csv.writer(open('/Users/huanxin/data_fetching/sequence/error.csv','w'),delimiter=',')
count=0
for i in IDs:
    i.remove('Borrower_id')
    for j in i:

# compute necessary info
#        j='411637'
        try:
            ip_name,ip_address,seq=sequence(j)
        except:
            count+=1
            print "very big error",j,count
            error.writerow([j])
            continue
        final_num=len(seq.keys())
        for k in seq.keys():
            town=''
            ip=''
            name=seq[k]['permanent_name']
            fellow=seq[k]['is_fellow']
            town=[seq[k]['display_location_city'],seq[k]['display_location_state'],seq[k]['display_location_country_name']]
#            lat,lng=google_map(town)
#            if (lat=='' and lng=='' and (town[0]!='' or town[1]!='' or town[2]!='')):
#                time.sleep(1)
#                lat,lng=google_map(town)
#                print '!!tried again!!'
#                print town,lat,lng
            for m in xrange(3):
                if town[m]==None:
                    town[m]=''
            if name in ip_name:
                ip=ip_address[ip_name.index(name)]
            location.writerow([j,final_num,name,ip,town[0]+', '+town[1]+', '+town[2]])
            order.writerow([j,final_num,name,fellow])
        if i.index(j)%10==0:
            print round(i.index(j)/float(len(i))*100,2),i.index(j),len(i)


