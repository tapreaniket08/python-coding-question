str1=str(input("Enter frist String"))
str2=str(input("Enter Second String"))
str1=str1.lower()
str2= str2.lower()
if len(str1)==len(str2):
    sor_str1=sorted(str1)
    sor_str2=sorted(str2)
    if sor_str1==sor_str2:
        print ("String is anagram")
    else:
        print("Strng is not anagram")    
else:
    print("String is not anagram")
