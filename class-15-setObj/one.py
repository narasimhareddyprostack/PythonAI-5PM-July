s={}
s1={10}
s2=set()
s3={10,20,30,10,20,30}
s4={10,20.5,True,10}
#read
print(type(s))  #<class 'dict'>
print(s1)       #{10}
print(s2)       #set()
print(s3)       #{10, 20, 30}  duplicates are not allowed
print(s4)       #{True, 10, 20.5} -no order guarentee