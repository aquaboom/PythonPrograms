#Given a list [5,4,3,2,1,-1], compute the addition of all positive numbers in a list

list1=[5,4,3,2,1,-1]
total=0
for j in list1:
    if j<=0:
        break
    total+= j
print(total)    
    
