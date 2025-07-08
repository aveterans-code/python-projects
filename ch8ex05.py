#ch8ex05


def isPrime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    factor = 3
    while factor < n:
        if n % factor == 0: return False
        factor = factor + 2
    return True

def main():
    print("Prime number tester")
    n = int(input("Enter a value to test: "))
    if isPrime(n):
        print(n,"is prime.")
    else:
        print(n, "is NOT prime.")

if __name__ == '__main__':
    main()
