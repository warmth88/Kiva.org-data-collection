#!/usr/bin python

import csv
f=open('country.csv','r')
location=[]
capita=[]
continent=[]
GDP_dic=csv.DictReader(f,dialect='excel')
for i in GDP_dic:
    location.append(i['Location'])
    capita.append(i['GDP per capita'])
    continent.append(i['Continent'])
for i in range(len(location)):
    if location[i]=='Cameroon':
        print 'yes'

f.close()
#def average_income(countries):

