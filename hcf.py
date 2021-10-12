x= int(input("Enter the  first number"))
y= int(input("Enter the second number"))
 
def hcf(num1,num2):
    if num1>num2:
        smaller=int(num1)
    else:
        smaller=int(num1)
    for i in range( 1, smaller+1):
        if (num1%i==0) and(num2%i==0):
            ans=i        
    return ans

print(f"hcf of two number{x,y} is:",hcf(x,y))    