print("select option ")
print("Addition :: 1")
print("Substraction :: 2")
print("multipliction :: 3")
print("Division :: 4")

while (True):
    chooce= int(input("Enter the choice in (1,2,3,4)"))
    if chooce in (1,2,3,4):
        n1= int(input("Enter the first number"))
        n2= int(input("Enter the sercond number"))

        if chooce==1:
            print("Addition of two number is", n1+n2)
        elif chooce==2:
            print("Substraction of two Number is",n1-n2)
        elif chooce==3:
            print("multipluction of two Number is",n1*n2) 
        elif chooce==4:
            print("Division of two Number is",n1/n2)           
            break
        
    else:
        print("Enter The valid input")