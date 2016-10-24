#!/usr/bin/python
import json
import urllib
import ordereddict

def sequence(ID):
    page=urllib.urlopen("http://www.kiva.org/lend/"+str(ID))
    page=page.read()
    start=page.find('Loan_LoanView')
    while page[start]!='{':
        start+=1
    end=start
    while page[end:end+16]!='show_all_lenders':
        end+=1

# find the ip locations of the lenders if availiable
    ip_name=[]
    ip_address=[]
    split1=page.find('}]}}')
    if split1==-1:
        split1=page.find('}]]}')
    tmp=page[start:split1+4]+'}'
    tmp=tmp.replace('null','""')
    ip_list=eval(tmp)
    for i in ip_list['lender_geocodes'].keys():
        try:
            key=ip_list['lender_geocodes'][i].keys()[0]
            ip_name.append(ip_list['lender_geocodes'][i][key][0]['permanent_name'])
            ip_address.append(i+' '+key)
        except:
            pass

# find the lending sequence
    split2=page.find('lendersJSON')
    seq=page[split2+14:end-3].translate(None,'\\')
    seq=seq.replace(' "Dia"','a')
    seq=seq.replace(' "Andy"','a')
    seq=seq.replace(' "veggie"','a')
    seq=seq.replace('"Tree"','a')
    seq=seq.replace('"T.J."','a')
#    print seq
    seq=json.loads(seq,object_pairs_hook=ordereddict.OrderedDict)

    return ip_name,ip_address,seq
