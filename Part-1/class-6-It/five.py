employees=[
    {'eid':101,'ename':'RG','avail':True,'esal':45000.45},
    {'eid':102,'ename':'SG','avail':False,'esal':55000.55},
    {'eid':103,'ename':'PG','avail':False,'esal':65000.65},
    {'eid':104,'ename':'NM','avail':True,'esal':None},
    {'eid':105,'ename':'AS','avail':True,'esal':95000.95},
]
#Iterate employees object using for loop and while loop
i=0
while i<=len(employees)-1:
    print(employees[i]['ename'])
    i=i+1