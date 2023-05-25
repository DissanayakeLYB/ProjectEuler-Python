#35 - circular prime

#finds the ceiling of a number
def ceil(n):
    if n%1 == 0:
        return n
    else:
        return (n//1)+1

def checkPrime(n):
    for i in range(1,(int(ceil(n**0.5))+1)):
        if n%i == 0 and i != 1:
            return False
        else:
            pass
    return True

def checkCircularPrime(n,primeList):
    num = list(n)
    for y in num:
        z = num[0]
        num.remove(z)
        if num == []:               #single digit primes are circular primes
            primeList.remove(n)
            return primeList
        elif:
            num.append(z)
            out = ""
            for p in num:
                out += str(p)
            if int(out) in primeList and n != int(out):
                primeList.remove(int(out))
                return checkCircularPrime(int(out),primeList)
            elif int(out) not in primeList and n != int(out):
                return False
            elif int(out) in primeList and n = int(out):
                return True
                


prime = [2]
circular prime = [2]
count = 1 #2 is already considered as a circular prime

for x in range(3,100):
    
    if checkPrime(x):
        prime.append(x)
        if checkCircularPrime(x,prime):
            count += 1
        else:
            if

    else:
        pass

print(count)
        
