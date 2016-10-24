from final_sequence import *
import csv


# open IDs list
IDs=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/error.csv','r'),delimiter=',')
location=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/final_location.csv','w'),delimiter=',')
location.writerow(['Borrower_ID','Lender_final_count','LenderID_ordered_by_lending','Lender_Geo_Location','Lender_HomeTown'])
order=csv.writer(open('/Users/wuhuanxin/data_fetching/sequence/final_order.csv','w'),delimiter=',')
order.writerow(['Borrower_ID','Lender_final_count','LenderID_ordered_by_lending','Is_Fellow'])

# get general info of lenders
f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_sequence.csv','r'),delimiter=',')
id_fellow=[]
for i in f:
    if i[3]!='no' and (i[2] not in id_fellow):
        id_fellow.append(i[2])

f=csv.reader(open('/Users/wuhuanxin/data_fetching/sequence/lending_locations_new.csv','r'),delimiter=',')
id_dic={}
count=0
for i in f:
#    if count==10:
#        break
    count+=1
    if i[2] not in id_dic:
        id_dic[i[2]]=i[3:]
print len(id_dic)

count=0
for i in IDs:
    print i[0]
#    if count==3:
#        break
    count+=1


    id_list,loc=sequence(i[0])
    print id_list
    print len(id_list)
    num=len(id_list)

    for j in id_list:
        if j in id_fellow:
            fellow='yes'
        else:
            fellow='no'
        order.writerow([i[0],num,j,fellow])

        if j in id_dic:
            location.writerow([i[0],num,j,id_dic[j][0],id_dic[j][1]])
        else:
            location.writerow([i[0],num,j,'',loc[id_list.index(j)]])

print count





