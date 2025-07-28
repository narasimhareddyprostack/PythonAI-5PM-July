fp=open('abc.txt','a')

print(fp.name)        #abc.txt
print(fp.mode)        #a 
print(fp.readable())  #False
print(fp.writable())  #True
print(fp.closed)      #False
fp.close()             
print(fp.closed)      #True
