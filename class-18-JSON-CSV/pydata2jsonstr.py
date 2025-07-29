import json 

employees=[
          {'eid': 101, 'ename': 'RG', 'avail': True, 'loc': None}, 
          {'eid': 102, 'ename': 'SG', 'avail': False,'loc': None}, 
          {'eid': 103, 'ename': 'PG', 'avail': True,'loc': None}
          ]
emp_json_str=json.dumps(employees)
print(emp_json_str)

#py Data to Json Str - json.dumps() method