enames=['Rahul','Sonia','Priyaka','NM','Amith',"Rahul"]
#index  0         1       2        3    4        5
#l.index(ele)  - return index value of specified element
print(enames.index('Sonia'))  #1
#print(enames.index('Satyna')) #ValueError
#l.count(ele) - return no of occurance
print(enames.count("Rahul"))  #2

#update 
enames.append('Vishwas')
print(enames)
enames.extend(['arif','sikindar'])
print(enames)

enames.reverse()

print(enames)

#how to sort list elemnts?
enames.sort()    #NSO ie A-Z or 0-9  asending order
print("After sorting-")
print(enames)