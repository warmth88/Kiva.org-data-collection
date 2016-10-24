#!/usr/bin/python
#
# This script get loans general data borrowers and lender's details from Kiva.com and sort it. The output format is CSV.
#
# Code written by Huanxin Wu for Prof. Yao's project.
#
# Version: 1.0
# Update history: 2012-3-15, 19:34PM-22:12PM
#                 2012-3-16, 11:54AM-16:22PM
#		  2012-3-16, 20:12PM-22:07PM
#		  2012-3-17, 13:25PM-16:12PM
#		  2012-3-17, 19:20PM-21:50PM
#		  2012-3-18, 16:04PM-21:34PM
#		  2012-3-19, 10:30AM-12:10PM
#		  2012-3-19, 13:30PM-16:23PM
#		  2012-3-19, 19:03PM-20:32PM
#		  2012-3-20, 13:12PM-17:23PM
#		  2012-3-21, 19:53PM-22:01PM


import urllib
import json
import time
import csv
from borrower import *
from lender import *
import os
#******************** This part is for generating the borrower_list.********************
# 1. Number of loans
# 2. The popularity ranking of loans
# 3. For each loan
#	a. Loan ID
#	b. The percentage has been raised
# 	c. Total amount of loan requests
#	d. If it is a group, the number of group members

# get total number of pages, page size and total loan number
fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity&status=fundraising")
fetch=json.loads(fetch.read())
total_pages=fetch['paging']['pages']
page_size=fetch['paging']['page_size']
total_loan=fetch['paging']['total']

# create CSV files and set default parameters
rank=1
loan_ID=0
name=name='borrower_list_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.csv'
prefix='/Users/huanxin/data_fetching/data/'
borrower_list=csv.writer(open(prefix+name,'w'),delimiter=',')
initial=['Ranking','LoanID','PercentageFunded','Amount','NumberOfMembers']
borrower_list.writerow(initial)

# scanning the whole list of loans
for i in xrange(total_pages):
	fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity"+"&status=fundraising"+"&page="+str(i+1))
	fetch=json.loads(fetch.read())
	for j in fetch['loans']:
		loan_ID=j['id']
		borrower_list.writerow([rank,loan_ID,'{:.2%}'.format(float(j['funded_amount'])/j['loan_amount']),j['loan_amount'],j['borrower_count']])
		rank+=1

	print i,'/',total_pages
print 'done successfully!'

#****************************************************************************************
"""
#******************** This part is for generating the borrower_page.*********************
loan_ID=0
borrower_page=csv.writer(open('borrower_page.csv','w'),delimiter=',')

# scanning the whole list of loans
for i in xrange(total_pages):
        fetch=urllib.urlopen("http://api.kivaws.org/v1/loans/search.json?sort_by=popularity"+"&status=fundraising"+"&page="+str(i+1))
        fetch=json.loads(fetch.read())
        for j in xrange(page_size):
                k=fetch['loans'][j]
                loan_ID=k['id']
                borrower_list.writerow(borrower(ID))
        print i,'/',total_pages

#****************************************************************************************

#******************** This part is for generating the lender_page.***********************
lender_ID=''
lender_page=csv.writer(open('lender_page.csv','w'),delimiter=',')

# scanning all the whole list of lenders.
fetch=urllib.urlopen("http://api.kivaws.org/v1/lenders/search.json?")
fetch=json.loads(fetch.read())
total_pages=fetch['paging']['pages']
page_size=fetch['paging']['page_size']

for i in xrange(total_pages):
	fetch=urllib.urlopen("http://api.kivaws.org/v1/lenders/search.json?page="+str(i+1))
	fetch=json.loads(fetch.read())
	for j in xrange(page_size):
		k=fetch['lenders'][j]
		lender_ID=k['lender_id']
		lender_page.writerow(lenders(lender_ID))
	print i,'/',total_pages

#****************************************************************************************
"""
