#29  - distinct powers

numbers = []
nums = 0

for a in range(2,101):
    for b in range(2,101):
        p = a**b
        if p in numbers:            #checks the number is already in the list
            pass
        else:
            numbers.append(p)       #collect the numbers
            nums += 1               #numbers counter
            
print(nums) #output the count
            
