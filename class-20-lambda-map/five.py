#print(list(map(lambda ename:ename.upper(),["rahul","sonia","priyanka"])))
enames=["rahul","sonia","priyanka"]

def change_case(name):
    return name.upper()

map_obj=map(change_case,enames)
print(list(map_obj))