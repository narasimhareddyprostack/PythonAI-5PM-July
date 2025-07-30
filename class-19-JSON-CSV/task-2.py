'''
read user_data.json file 
write userid,fname,age,gender in user.csv and user.json file
'''
import csv,json
fp1=open('user_data.json','r')
fp2=open('new_user.json','w')

user_data=json.load(fp1)
users=user_data['users']
#tranform for json file
new_users=[]
for user in users:
    new_users.append({'userid':user['id'],
                      'fname':user['firstName'],
                      'age':user['age'],
                      'gender':user['gender']
                      }
                     )

#print(new_users)
#load new_users into new_users.json file
json.dump(new_users,fp2)
print("New Json File Created")

fp1.close()
fp2.close()
