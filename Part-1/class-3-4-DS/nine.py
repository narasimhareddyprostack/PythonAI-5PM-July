emp={
    'eid':101,
    'ename':'Rahul',
    'gender':'Male'
}
print(emp)
#how to read dict values - using key name 
print(emp['eid'])
print(emp['ename'])
print(emp['gender'])
#print(emp['esal'])  #KeyError: 'esal'

#update
emp['ename'] = 'Rahul Gandhi'
print(emp)

#delete 
del emp['ename']

print(emp)