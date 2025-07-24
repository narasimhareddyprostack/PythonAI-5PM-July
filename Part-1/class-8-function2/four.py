def outer():
    print("Outer Function Started!")

    def inner():
        print("Inner Function")
    
    

outer()
inner() #NameError
#how to invoke - inner function from outer function