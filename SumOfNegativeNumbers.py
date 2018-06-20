#Add the values of a negative numbers and find the sum in a given list [10,7,6,5,4,3,-3,-4,-5,-2]


def SumOfNegativeNumbers():
   given_list=[10,7,6,5,4,3,-3,-4,-5,-2]         #The most efficient way will be to traverse from right side of the list
   sum=0
   i=len(given_list)-1                           #len function in python computes the length of the list
   while given_list[i]<0:                        #Checks if the value in the given list is negative i.e less than ZERO
       sum=sum+ given_list[i])
       j--
   print(sum)    
