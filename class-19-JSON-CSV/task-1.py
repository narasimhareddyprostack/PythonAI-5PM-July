'''
read user_data.json file 
write userid,fname,age,gender in user.csv and user.json file
'''
import csv,json
fp1=open('user_data.json','r')
user_data=json.load(fp1)
print(user_data)
users=user_data['users']
print(len(users))