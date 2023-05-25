#project euler 24

def krama(n):
    if n == 0:
        return 1
    else:
        return n * krama(n-1)

number = ""
j = 9 #kramaropitha creator
addition = 0 #the place of the number i.e. 1000000
i = [0,1,2,3,4,5,6,7,8,9] #the numbers possible to be used to make the number

while (addition < 1000000):
    
    p = -1                  
    value = krama(j)            #explained in onenote
    
    while (addition < 1000000):
        addition += value
        p += 1

    number += str(i[p])     #build the number
    i.remove(i[p])          #remove each digit used
    j -= 1
    
    if (addition == 1000000 and j == -1):   #if millionth number in the order is found and all the numbers are used, then stop the program
        print(number)
        break

    addition -= value
    
    

    


