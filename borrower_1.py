#!/usr/bin/python
import urllib
import csv
import json
import time
from borrower import *
import os

def total_lenders(ID):

        lenders_list_try=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json")
        lenders_list_try=json.loads(lenders_list_try.read())
        total=[lenders_list_try['paging']['total']]
        return total





fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity&status=fundraising")
fetch=json.loads(fetch.read())
total_pages=fetch['paging']['pages']

prefix='/Users/huanxin/data_fetching/data/'
name='borrower_1_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.csv'

borrower_1=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['Borrower_id','Country','Sector','Picture','LoanTerm(Months)','Repayment Schedule','Pre-distributed','Listed','Currency Exchange Loss','Default Protection','English_Description','Translated','Field Partner','Lender_So_Far']
borrower_1.writerow(initial)

for i in xrange(total_pages):
        fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity"+"&status=fundraising"+"&page="+str(i+1))
        fetch=json.loads(fetch.read())
        for j in fetch['loans']:
                loan_ID=j['id']
		total=total_lenders(loan_ID)
		borrower_detail=borrower(loan_ID)
		borrower_detail.append(total[0])
                borrower_1.writerow(borrower_detail)
        print i,'/',total_pages
print 'done successfully!'


