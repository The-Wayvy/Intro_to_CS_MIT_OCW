"""def SieveErastho(n):
        Primes = []
        Composites = []
        for num in range(2, n + 1):
                if not num in Composites:
                        if prime_or_not(num) == True:
                                Primes.append(num)
                                for mult in range(num + 1, n + 1):
                                        if mult % num == 0:
                                                Composites.append(mult)
                        else: Composites.append(num)
        else: return Primes                     
                

def prime_or_not(x):
        for integer in range(2, x):
                if x % integer == 0:
                        return False
                        break
        else: return True
                
print SieveErastho(25)"""

"""
Five layers of conditionals in the main function and 2 in the helper function.
The below solution has three layers, total.
Below is the superior version inspired by the Python Tutorial
"""
def erastho(total):
    prime = []
    for y in range(2, total + 1):
        for z in range(2, y):
            if y % z == 0:
                print y, 'is not prime'
                break
        else: prime.append(y)
    print "Presenting, the primes!", prime
                

erastho(25)



