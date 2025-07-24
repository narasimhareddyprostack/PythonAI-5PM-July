def outer():
    print("Outer Function Started!")

    def inner():
        print("Inner Function")
    
    #return 100
    return inner  #returning inner function ref


result=outer()
print(type(result))  #<class 'function'>
result()
result()

