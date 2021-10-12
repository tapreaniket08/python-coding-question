def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num=10
for i in range(0,num):
    print(fibo(i))




    
         