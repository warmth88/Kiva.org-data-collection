#!usr/bin/python

import urllib
import json
import time
import csv
from lender import *
name='partner_list_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+'.csv'
partner_list=csv.writer(open(name,'w'),delimiter=',')
initial=['PartnerID','Location','Status','RiskRating','Due_Diligence','TimeAtKiva','Entrepreneurs','Total_Loans','Interest_Fee','PortfolioYield','Profitability','AverageLoanSize','DelinquencyRate','LoansAtRiskRate','DefaultRate','LossRate']
partner_list.writerow(initial)

fetch=urllib.urlopen("http://api.kivaws.org/v1/partners.json?page=1")
fetch=json.loads(fetch.read())
count=0
page=1
for i in fetch['partners']:
	ID=i['id']
	partner_detail=field_partner(ID,page)
	partner_list.writerow(partner_detail)
	count+=1
	print count

fetch=urllib.urlopen("http://api.kivaws.org/v1/partners.json?page=2")
fetch=json.loads(fetch.read())
page=2
for i in fetch['partners']:
	ID=i['id']
	partner_detail=field_partner(ID,page)
	partner_list.writerow(partner_detail)
	count+=1
	print count
