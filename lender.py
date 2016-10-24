#!/usr/bin/python

# This module generates lenders_page automately from kiva.org identified by loan ID.

# 1. Location
# 2. Occupation
# 3. Member Since
# 4. How many loans in total
# 5. The IDs of those loans
# 6. How many teams
#	a. If nonzero, the IDs of those teams
#	b. For each team, how many loans
# 7. How many accepted invites
#	a. If nonzero, the IDs of those lenders
#	b. For each lender, how many loans
# 8. Portfolio Distribution
#	a. By gender: percentage of female borrower
#	b. By Country: Countries and the percentages
#	c. By sector: Sectors and the percentages

# This module also contains supporting functions for the program:
#	"field_partner" returns details of a certain field partner when the partner ID is provided.
#	"time_interval" calculates the time interval between two dates.
#	"loan_lenders" returns the lender list for an assigned loan ID.
#	"joined_teams" returns all the teams a specific lender joined when lender's ID is provided.
#	"lenders" returns details of a lender when his/her lender's ID is provided.


import urllib
import json
import time
import re
import codecs
import csv

def field_partner(partner_id,page):
	partner=urllib.urlopen("http://www.kiva.org/partners/"+str(partner_id))
	partner=partner.read()
	partner_total=urllib.urlopen("http://api.kivaws.org/v1/partners.json"+"?page="+str(page))
	partner_total=json.loads(partner_total.read())['partners']
	partner_detail=[partner_id]
	for i in partner_total:
		if i['id']==partner_id:
			location=''
			for j in i['countries']:
				location+=j['name']+'('+j['region']+') '
			partner_detail.append(location[:-1])
			partner_detail.append(i['status'])
			partner_detail.append(i['rating'])
			if i['due_diligence_type']=='Full':
				partner_detail.append('1')
			else: partner_detail.append('0')
			partner_detail.append(str(time_interval(i['start_date'][:-1],time.strftime("%Y-%m-%dT%H:%M:%S",time.gmtime()))-1))
			partner_detail.append(i['total_amount_raised'])
			break
	start=partner.find('>Kiva Entrepreneurs:')+len('>Kiva Entrepreneurs:')+17
	tmp=''
	while partner[start]!='<':
		tmp+=partner[start]
		start+=1
	partner_detail[6:6]=[tmp]

	start=partner.find('>Interest & Fees are Charged')+len('>Interest & Fees are Charged')+17
	interest_fees=partner[start:start+3]
	if interest_fees=='Yes':
		partner_detail.append('1')
	else: partner_detail.append('0')

	keywords=['>Portfolio Yield:','>Profitability<br/>(Return on Assets):','>Average Loan Size<br/>(% of Per Capita Income):','>Delinquency Rate:','>Loans at Risk Rate:','>Default Rate:','>Currency Exchange Loss Rate:']

	for i in keywords:
		tmp=''
		start=partner.find(i)+len(i)+17
		while partner[start]!='%':
			if partner[start:start+3]=='N/A':
				tmp='N/A'
				break
			if partner[start].isdigit() or partner[start]=='.' or partner[start]=='-':
				tmp+=str(partner[start])
			start+=1
		tmp+='%'
		if tmp=='N/A%':
			tmp='N/A'
		partner_detail.append(tmp)

	return partner_detail

def time_interval(time1,time2):
        t1=time.strptime(time1,"%Y-%m-%dT%H:%M:%S")
        t2=time.strptime(time2,"%Y-%m-%dT%H:%M:%S")
        return 12*(t2[0]-t1[0])+(t2[1]-t1[1])


def loan_lenders(ID):

	lenders_list_try=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json")
	lenders_list_try=json.loads(lenders_list_try.read())
	lenders_detail=[lenders_list_try['paging']['total']]
	lender_IDs=[]
	team_IDs=[]
	for i in range(lenders_list_try['paging']['pages']):
		lenders_list=urllib.urlopen("http://api.kivaws.org/v1/loans/"+str(ID)+"/lenders.json?page="+str(i+1))
		lenders_list=json.loads(lenders_list.read())
		for j in lenders_list['lenders']:
			lender_IDs.append(j['lender_id'])
			team_IDs.extend(joined_teams(j['lender_id'])[1])
	lenders_detail.append(lender_IDs)
	lenders_detail.append(team_IDs)

	return lenders_detail

def joined_teams(lender_id):
    joined_teams_list_try=json.loads(urllib.urlopen("http://api.kivaws.org/v1/lenders/"+lender_id+"/teams.json").read())
    #teams_list=[]
    team_number=0
    #team_loans=[]
    total_teams=joined_teams_list_try['paging']['total']
    for i in range(joined_teams_list_try['paging']['pages']):
        joined_teams_list=json.loads(urllib.urlopen("http://api.kivaws.org/v1/lenders/"+lender_id+"/teams.json?page="+str(i+1)).read())
        team_number+=len(joined_teams_list['teams'])
    return team_number


#		for j in joined_teams_list['teams']:
#			teams_list.append(j['id'])
#			team_loans.append(j['loan_count'])
#	return [total_teams,teams_list,team_loans]



def lenders(ID):
    lender=urllib.urlopen("http://www.kiva.org/lender/"+ID)
    lender=lender.read()
    lender_api=urllib.urlopen("http://api.kivaws.org/v1/lenders/"+ID+".json")
    lender_api=json.loads(lender_api.read())
    lender_page=[lender_api['lenders'][0]['lender_id']]
    if lender_api['lenders'][0]['whereabouts']!='':
        try:
            lender_page.append(lender_api['lenders'][0]['whereabouts'].encode('ascii', 'ignore')+','+lender_api['lenders'][0]['country_code'])
        except:
            lender_page.append(lender_api['lenders'][0]['whereabouts'])
    else: lender_page.append('')
	#lender_page.append(lender_api['lenders'][0]['occupation'])
    lender_page.append(lender_api['lenders'][0]['member_since'][:-10])
    lender_page.append(lender_api['lenders'][0]['loan_count'])

    tmp=joined_teams(ID)
#	lender_page.append(tmp[0])
#	lender_page.append(tmp[1])
#	lender_page.append(tmp[2])
    lender_page.append(tmp)
    lender_page.append(lender_api['lenders'][0]['invitee_count'])
#	for start in re.finditer('http://www.kiva.org/lender/',lender):
#		tmp=''
#		k=start.end()
#		invites_detail=[]
#		while lender[k]!='"' and lender[k]!="?" and lender[k]!="'":
#			tmp+=lender[k]
#			k+=1
#		if tmp!=ID:
#			invites=urllib.urlopen("http://api.kivaws.org/v1/lenders/"+tmp+".json")
#			invites=json.loads(invites.read())
#			invites_detail.append([tmp,invites['lenders'][0]['loan_count']])

#	lender_page.append(invites_detail)

    gender=[]
   #keywords=["data.addColumn('number','gender')","data.addColumn('number','country')","data.addColumn('number','sector')"]
    keywords=["data.addColumn('number','gender')"]
    for keys in keywords:
        k=lender.find(keys)+35
        while lender[k:k+3]!='var':
            tmp=''
            start=k
            if lender[k]=="'":
                k+=1
                while lender[k]!="'": k+=1
                gender.append(lender[start+1:k])
            if lender[k-3:k]==',1,':
                while lender[k]!=')':
                    k+=1
                    tmp+=lender[k-1]
                gender.append(tmp)
            k+=1
    female_ratio='0.00'
    for i in range(len(gender)):
        if gender[i]=='Female':
            female_ratio=gender[i+1]

    countries=[]
    country_portion=[]
    keywords=["data.addColumn('number','country')"]
    for keys in keywords:
        k=lender.find(keys)+35
        while lender[k:k+3]!='var':
            tmp=''
            start=k
            if lender[k]=="'":
                k+=1
                while lender[k]!="'": k+=1
                countries.append(lender[start+1:k])
            if lender[k-3:k]==',1,':
                while lender[k]!=')':
                    k+=1
                    tmp+=lender[k-1]
                country_portion.append(tmp)
            k+=1
    prefix='/Users/huanxin/data_fetching/'
    f=open(prefix+'country.csv','r')
    location=[]
    capita=[]
    continent=[]
    GDP_dic=csv.DictReader(f,dialect='excel')
    for i in GDP_dic:
        location.append(i['Location'])
        capita.append(i['GDP per capita'])
        continent.append(i['Continent'])
    average_income=0.0
    for i in countries:
        for j in xrange(len(location)):
            if i==location[j]:
                average_income+=float(capita[j])
                break
    if len(countries)!=0:
        average_income=average_income/(len(countries))

    lender_page.append(female_ratio)
    lender_page.append("%.2f" % average_income)

    f.close()

    name='error_'+time.strftime('%y')+time.strftime('%m')+time.strftime('%d')+time.strftime('%H')+'.txt'
    prefix='/Users/huanxin/data_fetching/data/'
    f=open(prefix+name,'a')
    portion={'Middle East':0.0,'Asia':0.0,'Africa':0.0,'Eastern Europe':0.0,'South America':0.0,'Central America':0.0,'North America':0.0}
    for i in xrange(len(countries)):
        for j in xrange(len(location)):
            if countries[i]==location[j]:
                try:
                    portion[continent[j]]+=float(country_portion[i])
                except:
                    f.write(ID)
                    f.write('\n')
    for i in portion.keys():
        lender_page.append(round(portion[i],2))

    f.close()


    id_list=[]
    loan_ids=json.loads(urllib.urlopen("http://api.kivaws.org/v1/lenders/"+ID+"/loans.json").read())
    pages=loan_ids['paging']['pages']
    for i in xrange(pages):
        loan_ids=json.loads(urllib.urlopen("http://api.kivaws.org/v1/lenders/"+ID+"/loans.json").read())
        for j in loan_ids['loans']:
            id_list.append(j['id'])
    for i in id_list:
        lender_page.append(i)




    return lender_page

