#! /usr/bin/python
import urllib
import csv
import json
import time
import os

def loan_lenders(ID):
    lenders_list_try=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json")
    lenders_list_try=json.loads(lenders_list_try.read())
    total_lenders=[lenders_list_try['paging']['total']]
    lender_IDs=[]
    for i in range(lenders_list_try['paging']['pages']):
        lenders_list=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json?page="+str(i+1))
        lenders_list=json.loads(lenders_list.read())
        for j in lenders_list['lenders']:
            try:
                lender_IDs.append(j['lender_id'])
            except:
                lender_IDs.append('Anonymous')
    return total_lenders,lender_IDs




fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity&status=fundraising")
fetch=json.loads(fetch.read())
total_pages=fetch['paging']['pages']

name=name='borrower_2_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.csv'
prefix='/Users/huanxin/data_fetching/data/'



borrower_2=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['Borrower_id','Lender_So_Far','LenderID']
borrower_2.writerow(initial)

for i in xrange(total_pages):
    fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity"+"&status=fundraising"+"&page="+str(i+1))
    fetch=json.loads(fetch.read())
    for j in fetch['loans']:
        loan_ID=j['id']
        total,lenders=loan_lenders(loan_ID)
        for k in lenders:
            borrower_2.writerow([loan_ID,total[0],k])
    print i,'/',total_pages
print 'done successfully!'


