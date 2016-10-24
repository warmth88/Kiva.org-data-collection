#!/usr/bin/python
import urllib
import re

def sequence(ID):
    page=urllib.urlopen("http://www.kiva.org/lend/"+str(ID))
    page=page.read()
    start=page.find('business_id')
    page=page[start:]
    pos=[m.start() for m in re.finditer('permanent_name',page)]
    loc1=[m.start() for m in re.finditer('display_location_city',page)]
    loc2=[m.start() for m in re.finditer('display_location_state',page)]
    loc3=[m.start() for m in re.finditer('display_location_country_name',page)]
    print len(loc1),len(loc2),len(loc3)

    id_list=[]
    for i in pos:
        i=i+16
        while page[i]!='"':
            i+=1
        start=i+1
        i+=1
        while page[start-1]=='"' and page[i]!='"':
            i+=1
        end=i-2
        id_list.append(page[start:end])

    loc_city=[]
    for i in loc1:
        i=i+23
        if page[i+1:i+5]=='null':
            loc_city.append('')
            continue
        while page[i]!='"':
            i+=1
        start=i+1
        i+=1
        while page[start-1]=='"' and page[i]!='"':
            i+=1
        end=i-1
        loc_city.append(page[start:end])

    loc_state=[]
    for i in loc2:
        i=i+24
        if page[i+1:i+5]=='null':
            loc_state.append('')
            continue
        while page[i]!='"':
            i+=1
        start=i+1
        i+=1
        while page[start-1]=='"' and page[i]!='"':
            i+=1
        end=i-1
        loc_state.append(page[start:end])

    loc_country=[]
    for i in loc3:
        i=i+31
        if page[i+1:i+5]=='null':
            loc_country.append('')
            continue
        while page[i]!='"':
            i+=1
        start=i+1
        i+=1
        while page[start-1]=='"' and page[i]!='"':
            i+=1
        end=i-1
        loc_country.append(page[start:end])

    loc=[]
    for i in xrange(len(loc1)):
        loc.append(loc_city[i]+', '+loc_state[i]+', '+loc_country[i])
    print loc

    return id_list,loc
