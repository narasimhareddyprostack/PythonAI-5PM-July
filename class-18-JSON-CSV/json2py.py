import json 
emp_json_str='''
 [{"eid":101,"ename":"RG","avail":true,"loc":null},
  {"eid":102,"ename":"SG","avail":false},
  {"eid":103,"ename":"PG","avail":true}
 ]
'''
employees=json.loads(emp_json_str)
print(employees)