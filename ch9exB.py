#ch9exB

from random import random, seed

def main():
    seed(123456)
    printIntro()
    n = getInputs()
    printNumbers(n)

def printIntro():
    print("This program generates n random numbers")

def getInputs():
    n = int(input("How many numbers? "))
    return n

def printNumbers(n):
    for i in range(n):
        print(f'{random():0.5f}')

if __name__ == "__main__":
    main()
