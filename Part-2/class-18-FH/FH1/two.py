#read abc.txt and write in new file ie data.txt
fp1=open('abc.txt','r')
data=fp1.read()

fp2=open('data.txt','a')
fp2.write(data)
print("New File created and written success")

fp1.close()
fp2.close()