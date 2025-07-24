ba=bytearray([10,40,60,155,81,31,18,232])

print(ba)        #bytearray(b'\n(<\x9bQ\x1f\x12\xe8')
print(type(ba))  #<class,bytearray>
ba[0] = 101

for num in ba:
    print(num)


#bytearray - is Mutable Object