eids=set()
print(eids)

#add element to set object 
eids.add(101)
print(eids)
#add multiple elements
#eids.update(102)  #TypeError

eids.update({102,103,104})
print(eids)