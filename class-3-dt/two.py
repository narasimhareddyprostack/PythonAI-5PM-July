b=bytes([10,40,60,155,81,31,18,232])
print(b)        #b'\n(<\x9bQ\x1f\x12\xe8'
print(id(b))    #address - int format
print(type(b))  #<class,bytes>

#print all bytes values
for value in b:
    print(value)