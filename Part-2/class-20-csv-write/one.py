import csv 

users=[
        (101,'Rahul',45000),
        (102,'Sonia',55000),
        (103,'Priya',65000),
      ]
fp=open('congressuser.csv','w',newline='')
cw = csv.writer(fp)
cw.writerow(['userid','uname','salary'])
cw.writerows(users)
print("New CSV created")

fp.close()