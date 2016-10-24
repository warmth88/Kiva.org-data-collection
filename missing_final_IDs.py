import urllib
import json
import time
import csv
from borrower_for_all import *
import os
import codecs
import sys


"""
# open file for read
file_list=os.listdir('/Users/wuhuanxin/data_fetching/missing/')
ID_list=[]
for i in file_list:
    file_open=csv.reader(open('/Users/wuhuanxin/data_fetching/missing/'+i,'r'),delimiter=',')
    for j in file_open:
        if j[0] in ID_list:
            pass
        else:
            ID_list.append(j[0])
    ID_list=ID_list[1:]
    ID_cache=csv.writer(open('/Users/wuhuanxin/data_fetching/missing/IDs.csv','w'),delimiter=',')
    ID_cache.writerow(ID_list)
print len(file_list)
print len(ID_list)

"""
def total_lenders(ID):

    lenders_list_try=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json")
    lenders_list_try=json.loads(lenders_list_try.read())
    total=[lenders_list_try['paging']['total']]
    return total


ID_cache=csv.reader(open('/Users/wuhuanxin/data_fetching/missing_final/missing_IDs.csv','r'),delimiter=',')
ID=[]
for i in ID_cache:
    if i[0]=='borrower_id' or i[0]=='LoanID':
        pass
    else:
        ID.append(i[0])
print ID
print len(ID)

prefix='/Users/wuhuanxin/data_fetching/missing_final/'
name='all_loans_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.csv'

all_loans=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['Borrower_id','Country','Sector','Picture','LoanTerm(Months)','Repayment Schedule','Pre-distributed','Listed','Currency Exchange Loss','Default Protection','English_Description','Translated','Field Partner','Borrower Count','Female Percentage','Lender Count','Country Code','Town','Geo Location','Activity','Funded Date','Loan Amount','Funded Amount','Planned Expiration Date','Status']
all_loans.writerow(initial)
count=0
for i in ID:
    loan_ID=i
    try:
        total=total_lenders(loan_ID)
    except:
        total=['error']

    fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(loan_ID)+".json")
    fetch=json.loads(fetch.read())
    j=fetch['loans'][0]

    temp=borrower(loan_ID)
    borrower_detail=temp[:-2]
    borrower_detail.append(len(j['borrowers']))
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
#    time.sleep(.5)
    count+=1
    if count%20==0:
        print round(float(count)/len(ID)*100,2),count,len(ID)
print 'done successfully!'



