fp=open('abc.txt')
#print(fp.__dict__)  #{'mode': 'r'}
#data=fp.readlines()
data=fp.readline(5)
print(data)