#ch11ex10.py

def sieve(n):
    # All values start here
    candidates = list(range(2, n+1))
    primes =[] # Starts the empty list
    while len(candidates) > 0: #outer while
        nextPrime = candidates.pop(0) # Removes first item from list
        primes.append(nextPrime)
        indx = 0
        while indx < len(candidates): #inner while
            if candidates[indx] % nextPrime == 0:
                candidates.pop(indx)
            else:
                indx += 1
    return primes

def main():
    print("Sieve of Eratosthenes\n")
    n = int(input("Enter Upper Limit: "))
    primes = sieve(n)
    print(primes)

if __name__ == '__main__':
    main()
