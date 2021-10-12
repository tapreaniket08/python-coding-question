def add(num):
    if num<=1:
        return num 
    else:
        return num +add(num-1)

number=10
print(f"Addition of the number:{number}==",add(number))
