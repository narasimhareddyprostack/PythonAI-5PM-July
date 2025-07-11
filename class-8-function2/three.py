def outer():
    print("Outer Function Started!")

    def inner():
        print("Inner Function")
    
    inner()
    inner()

outer()