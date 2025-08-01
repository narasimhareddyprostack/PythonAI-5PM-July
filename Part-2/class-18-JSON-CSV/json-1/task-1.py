#read usrers.json file and write into new json file.
import json
fp1=open('users.json','r')
users=json.load(fp1)

print(len(users))
print(type(users))
print(users)