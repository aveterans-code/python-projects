#ch9exC.py
from random import randrange, seed

def main():
    seed(123456)
    printIntro()
    n = getInputs()
    results = generateSamples(n)
    printSummary(n, results)

def printIntro():
    print("Confirm PRNs are uniform")

def getInputs():
    n = int(input("How many samples would you like? "))
    return n

def generateSamples(n):
    results = [0,0,0,0,0,0]
    for i in range(n):
        sample = randrange(0,6)
        #results[sample] = results[sample] + 1
        results[sample] += 1
    return results

def printSummary(n, results):
    for i in range(0,6):
        print(f'{i}: {results[i]/n:6.2%}')

if __name__ == "__main__":
    main()
