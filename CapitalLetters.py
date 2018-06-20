#Count no. of capital letters in a given file

import os

def Capfunc():  # Function definition to find the capital letters in a file                  
    os.chdir("C:\\Users\\Sonali\\Desktop")
    with.open('Filname.txt')as filename:
        count=0
        for element in filename.read():
            if element.isupper():
                count+=1
        filename.close()        
        print(count)        
    
