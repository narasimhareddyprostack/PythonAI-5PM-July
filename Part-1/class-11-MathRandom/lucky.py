from random import choice
employees_List = [
    "satya","Vishnavi","Jahnavi","RG","SG","PG","NM"
]


print(type(employees_List))

for x in range(3):
    print(choice(employees_List))
