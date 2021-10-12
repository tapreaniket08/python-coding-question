x= int(input("Enter the first number"))
y= int(input("Enter the secomd number"))

def lcm(num1,num2):
     if num1>num2:
         gratter=num1
     else:
         gratter=num2

     while(True):
        if(gratter%num1==0) and (gratter%num2==0):
            ans= gratter
            break
        gratter +=1 
    
     return ans 

print(f"LCM of the number {x,y} is", lcm(x,y))
