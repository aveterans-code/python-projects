#ch11ex5

def count(myList, x):
    ans = 0
    for item in myList:
        if item == x:
            ans = ans + 1
    return ans

def isin(myList, x):
    for item in myList:
        if item == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
    return None

def reverse(myList):
    for i in range(len(myList) // 2):
        j = -(i+1)
        myList[i], myList[j] = myList[j], myList[i]


def main():
    a = [27,64,60,13,20,62,64,17,80,58,71,90]
    print(count(a, 64))
    print(count(a, 11))
    print(isin(a, 17))
    print(isin(a, 23))
    print(index(a, 20))
    print(a)
    reverse(a)
    print(a)

if __name__ == '__main__':
    main()
