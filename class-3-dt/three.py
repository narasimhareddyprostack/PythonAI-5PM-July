b=bytes([10,40,60,155,81,31,18,232])
#indexing 0  1  2  3   4  5 6  7
print(b)        #b'\n(<\x9bQ\x1f\x12\xe8'
print(id(b))    #address - int format
print(type(b))  #<class,bytes>

b[0] = 100

#TypeError: 'bytes' object does not support item assignment
#bytes - Object is immutable