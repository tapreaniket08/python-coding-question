

if __name__=="__main__":
   num= int(input("Enter the no of data"))
   l1=[]
   for i in range(num):
       data=input("input data")
       l1.append(data)
   l1=list(set(l1))
   print(l1)
