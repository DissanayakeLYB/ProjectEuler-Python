#34 - digit factorials

#function to calculate kramaropitha
def krama(n):
    if n==0:
        return 1
    else:
        return (n*krama(n-1))

i = 145     #first starting value

numbers = []

while (i<99999999):     #maximum possbile upperbound
    addition = 0
    
    for x in str(i):                    #creates the number
        addition += (krama(int(x)))

    if addition == i:
        numbers.append(i)

    i += 1

print(numbers)
print(sum(numbers))

"""the possibility for this to happen can be found as 9! = 362880 , times which number will be less than the number of digits used.
that means,  9! * p must have less digits than p. and the suitable value for p is 8. therfore
considering only until 99 999 999 is enough."""
    
