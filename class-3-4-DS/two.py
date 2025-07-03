#create - List
eids=[101,102,103,103]
a=[10,20.5,'RG',True,10,20.5] 
enames=['Rahul','Sonia','Priyanka','Modi']
#read   - list
print(enames)
#how to read list elements
print(enames[0]) #Rahul
#print(enames[20]) #IndexError: list index out of range
#update - list elements
enames[0] = 'Rahul Gandhi'
print(enames)
#delete list elements

enames.remove('Sonia')

print(enames)
enames.clear()
print(enames)