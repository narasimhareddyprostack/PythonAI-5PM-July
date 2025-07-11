def outer():
    print("Outer Function Started!")

    def inner():
        print("Inner Function")
    
    #return 100
    return inner  #returning inner function ref


inner=outer()
print(type(inner))  #<class 'function'>
inner()
inner()

