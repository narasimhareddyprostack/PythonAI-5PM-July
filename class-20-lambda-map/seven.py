numbers=[18,31,8,11,7,55,232]
#collect all even numbers in list
def verify_num(num):
    return num%2==0

even_nums=list(filter(verify_num,numbers))
print(numbers)
print(even_nums)
