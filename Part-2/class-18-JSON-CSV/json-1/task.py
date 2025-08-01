#read usrers.json file and write into new json file.
import json
fp1=open('users.json','r')
fp2=open('emp.json','w')

employees=json.load(fp1)

json.dump(employees,fp2)
print('New Json File Created!')
