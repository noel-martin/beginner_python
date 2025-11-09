str1= input("Enter array elements with spaces: ")
target=int(input("Enter the target: "))
l1= str1.split()
for i in range (0,len(l1)):
    for j in range (0,len(l1)):
        s= int(l1[i])+int(l1[j])
        if s==target:
            x= f"{i} {j}"
            l2= x.split()
            break
print(l2)