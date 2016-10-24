   #!/usr/bin/python
#
# This script get loans general data borrowers and lender's details from Kiva.com and sort it. The output format is CSV.
#
# Code written by Huanxin Wu for Prof. Yao's project.
#
# Version: 1.0
# Update history: 2012-7-04, 18:34PM-22:12PM

import urllib
import json
import time
import csv
from borrower_for_all import *
import os
import codecs
import sys

def total_lenders(ID):

    lenders_list_try=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json")
    lenders_list_try=json.loads(lenders_list_try.read())
    total=[lenders_list_try['paging']['total']]
    return total


fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?")
fetch=json.loads(fetch.read())
total_pages=fetch['paging']['pages']

prefix='/Users/huanxin/data_fetching/data/'
name='all_loans3_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'_'+str(sys.argv[1])+'.csv'

all_loans=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['Borrower_id','Country','Sector','Picture','LoanTerm(Months)','Repayment Schedule','Pre-distributed','Listed','Currency Exchange Loss','Default Protection','English_Description','Translated','Field Partner','Borrower Count','Female Percentage','Lender Count','Country Code','Town','Geo Location','Activity','Funded Date','Loan Amount','Funded Amount','Planned Expiration Date','Status']
all_loans.writerow(initial)
print total_pages
for i in xrange(21544,21545):
    if i%int(sys.argv[2])==int(sys.argv[1]):
        fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?"+"page="+str(i+1))
        fetch=json.loads(fetch.read())
        for j in fetch['loans']:
            loan_ID=j['id']
            try:
                total=total_lenders(loan_ID)
            except:
                total=['error']
            temp=borrower(loan_ID)
            borrower_detail=temp[:-2]
            borrower_detail.append(j['borrower_count'])
            borrower_detail.append(temp[-2])
            borrower_detail.append(total[0])
            borrower_detail.append(j['location']['country_code'])
            try:
                borrower_detail.append(j['location']['town'].encode('ascii','ignore'))
            except:
                borrower_detail.append('')
            try:
                borrower_detail.append(j['location']['geo']['pairs'])
            except:
                borrower_detail.append('')
            borrower_detail.append(j['activity'])
            borrower_detail.append(temp[-1])
            borrower_detail.append(j['loan_amount'])
            borrower_detail.append(j['funded_amount'])
            try:
                borrower_detail.append(j['planned_expiration_date'][:10])
            except:
                borrower_detail.append('')
            borrower_detail.append(j['status'])
            all_loans.writerow(borrower_detail)
            time.sleep(.5)
    if (i-int(sys.argv[1]))%1==0:
        print round(float(i)/21543*100,2),i,21543,sys.argv[1]
print 'done successfully!'



