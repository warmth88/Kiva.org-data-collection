#!/usr/bin/python 

# This module generates borrowers_page automately from kiva.org identified by Loan ID.
# 
# 1. Location, e.g., Medellin, Columbia
# 2. Sector, e.g., Services|Internet Coffee
# 3. Is a picture displayed (1/0)?
# 4. Loan details:
# 	a. Repayment Term, e.g., 26 months
# 	b. Repayment Schedule, e.g. Monthly
# 	c. Pre-Disbursed, e.g., Feb 8, 2012
# 	d. Listed, e.g., Mar 5, 2012
#	e. Currency Exchange Loss:
#	f. Default Protection
# 5. Language used in the loan description (e.g., Jose has been a hard worker his whole life)
#	a. Is the original description is in English (1/0)?
#	b. If not, is it translated into English (1/0)?
# 6. Field Partner
#	a. Identity (not necessary the full name, ideally a unique ID number)
#	b. Risk rating (star rating)
#	c. Due Diligence Type (Full or Basic)
#	d. Time at Kiva
#	e. Entrepreneurs
#	f. Total loans
#	g. Interest & Fees are Charged:
#		g.i. Yes or No
#		g.ii. Portfolio Yield
#		g.iii. Profitability
#		g.iv. Average Loan Size
#		g.v. Delinquency Rate
#		g.vi. Loans at Risk Rate
#		g.vii. Default Rate
#		g.viii. Loss Rate
# 7. Lenders
#	a. How many lenders so far?
#	b. For the lenders who are not "Anonymous"
#		b.i. Lender ID
#	c. Contributing Teams
#		c.i. Team ID

import urllib
import json
import time
import csv
from lender import time_interval

def borrower(ID):
# fetch information of a particular borrower.

# get specific loan's info and short dictionary representation for convenience.
        item=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+".json")
        item=json.loads(item.read())
        item=item['loans'][0]
        loan_amount=item['terms']['loan_amount']
        pre_disbursed=item['terms']['disbursal_date'][0:-1]
        scheduled_payments=item['terms']['scheduled_payments']

# write loan_ID, location, sector, pictures(Y/N) to the borrower page
	borrower_page=[ID]
	borrower_page.append(item['location']['country'])
	borrower_page.append(item['sector'])
	borrower_page.append(str(int(item['borrowers'][0]['pictured'])))
	
# ****************loan details*************************
	first_pay=scheduled_payments[0]['due_date'][:-1]
	repayment_schedule='Irregularly'
	for i in scheduled_payments:
		if i['due_date'][:-1]!=first_pay:
			if time_interval(first_pay,i['due_date'][:-1])==1:
				repayment_schedule='Monthly'
        if scheduled_payments[-1]['amount']==loan_amount:
                repayment_schedule='At end of term'

# calculate repayment term
        repayment_term=str(time_interval(pre_disbursed,scheduled_payments[-1]['due_date'][:-1])) 
# when posted
        listed=item['posted_date'][:-1]

# currency exchage loss
        if item['terms']['loss_liability']['currency_exchange']=='shared':
                exchange_loss='Possible'
        elif item['terms']['loss_liability']['currency_exchange']=='none':
                exchange_loss='N/A'
        else:
                exchange_loss='Covered'

# default protection
        if item['terms']['loss_liability']['nonpayment']=='lender':
                default_protection='Not Covered'
        else:
                default_protection='Covered'

	if exchange_loss=='Covered': exchange_loss=1
	if exchange_loss=='Possible': exchange_loss=0
	if default_protection=='Not Covered': default_protection=0
	else: default_protection=1
	borrower_page.append(repayment_term)
	borrower_page.append(repayment_schedule)
	borrower_page.append(pre_disbursed[:10])
	borrower_page.append(listed[:10])
	borrower_page.append(exchange_loss)
	borrower_page.append(default_protection)
#*****************************************************

#**************language used**************************
# orginal description in English?
        lan=item['description']['languages']
        if len(lan)==1 and lan[0]=='en':
                original_English=1
                translated_English=0
        elif len(lan)!=1:
		original_English=0
                translated_English=1
        else:
                original_English=0
                translated_English=0

        borrower_page.append(str(original_English))
	borrower_page.append(str(translated_English))
	borrower_page.append(item['partner_id'])
#*****************************************************

# field partner
#        borrower_page.append(field_partner(item['partner_id']))

# lenders info
#	borrower_page.append(loan_lenders(ID))	

	return borrower_page

