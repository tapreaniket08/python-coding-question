n=int(input("Enter the number"))
print("Entered Numbered",n)
result=0
while n!=0:
    result=result*10+n%10
    n=n//10
print("reverse number is :",result)