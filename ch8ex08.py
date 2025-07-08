#ch8ex08.py
    #Euclids algorithm

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("Calculates the Greatest Common Divisor with Euclids algorithm\n")

    a, b = eval(input("Enter two natural numbers (n1, n2): "))

    print(f"The GCD of {a} and {b} is: {gcd(a, b)}\n")

if __name__ == '__main__':
    main()
