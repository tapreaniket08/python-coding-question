n= int(input("Enter the Number"))
i=0
number=n
temp=n
result=0
while n!=0:
    n=(n//10)
    i=i+1
while number!=0:
    n=number%10
    result=result+pow(n,i)
    number=(number//10)
if temp==result:
    print(f"number is amstrong {temp}=={result}")
else:
    print(f"number is not amstrong {temp}!={result}")
     