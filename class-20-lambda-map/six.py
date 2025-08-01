numbers=[18,31,8,11,7,55,232]
#collect all even numbers in list
even_nums=[]

for num in numbers:
    if num%2==0:
        even_nums.append(num)
        
print(numbers)
print(even_nums)
