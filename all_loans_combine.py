#!/usr/bin/python

file_num=7 #input('input total file numbers')
prefix='/Users/huanxin/data_fetching/data/'
name1='all_loans.csv'
f=open(prefix+name1,'w')

id_list=[]
for i in xrange(int(file_num)):
    name='all_loans_'+str(i+1)+'.csv'
    f1=open(prefix+name,'r')
    for line in f1:
        id=''
        for j in line:
            if j!=',':
                id+=j
            else: break
        if (id in id_list):
            pass
        else:
            f.write(line)
            id_list.append(id)
    f1.close()
f.close()

