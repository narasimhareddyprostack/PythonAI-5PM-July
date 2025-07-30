'''
read user_data.json file 
write userid,fname,age,gender in user.csv and user.json file
'''
import csv,json
fp1=open('user_data.json','r')
fp2=open('new_user.json','w')
fp3=open('user.csv','w',newline="")

user_data=json.load(fp1)
users=user_data['users']
#tranform for json file
new_users=[]
csv_users=[]
for user in users:
    new_users.append({'userid':user['id'],'fname':user['firstName'],'age':user['age'],'gender':user['gender']})
    csv_users.append((user['id'],user['firstName'],user['age'],user['gender']))

#print(new_users)
#print(csv_users)
#load new_users into new_users.json file
json.dump(new_users,fp2)
print("New Json File Created")

#load csv_users in user.csv file
csvwriter=csv.writer(fp3)
csvwriter.writerow(['userid','fname','age','gender'])
csvwriter.writerows(csv_users)
print("New CSV File Created!")

fp1.close()
fp2.close()
fp3.close()