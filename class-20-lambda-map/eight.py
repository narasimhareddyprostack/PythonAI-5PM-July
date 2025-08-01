numbers=[18,31,8,11,7,55,232]
print(numbers)
#collect all even numbers in list
#print(list(filter()))
print(list(filter(lambda num:num%2==0,numbers)))