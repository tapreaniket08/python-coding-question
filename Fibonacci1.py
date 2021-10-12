num=int(input("How many numbers you want?"))
#sol no 1
"""
n1=0
n2=1
for i in range(num):
     print(n1)
     temp=n1+n2
     n1=n2
     n2=temp  
    
"""

# sol no2
n1,n2=0,1
count=0
while count<num:
    print (n1)
    temp=n1+n2
    n1=n2
    n2=temp
    count+=1