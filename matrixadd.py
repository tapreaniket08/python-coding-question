m1=[
    [1,5,6],
    [7,9,8],
    [12,15,5]
]
m2=[
    [11,25,16],
    [17,59,88],
    [2,25,15]
]

for i in range(0,len(m1)):
    for j in range(0,len(m1[0])):
       m1[i][j]=m1[i][j]+m2[i][j]

for i in m1:
   print(i) 