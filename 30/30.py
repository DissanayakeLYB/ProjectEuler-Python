#30 - digit fifth powers

i = 1000        #starting point
output = []     #the numbers that can be represented as the sum of fifth powers of the digits used in that number

while i < 999999:   #maximum possibility. explained in the notepad
    addition = 0
    
    for x in str(i):
        addition += (int(x)**5)

    if addition == i:               #the necessity
        output.append(i)

    i += 1

print(output)
print(sum(output))
