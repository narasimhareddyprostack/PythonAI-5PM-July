numbers=(18,31,8,11,7,55)
#numbers.sort()  #AttributeError

#how to sort tuple elemnts - using inbuilt function ie
# sorted
new_numbers=tuple(sorted(numbers,reverse=True))
print(new_numbers)