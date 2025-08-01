emp={
    'eid':101,
    'ename':'Rahul Gandi',
    'esal':45000.45,
}
#print(emp['loc'])  #KeyError
print(emp.get('eid'))  # 101
print(emp.get('loc'))