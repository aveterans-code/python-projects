#ch6ex13.py
#create and modify a list of numbers

def toNumbers(aList):

    for i in range(len(aList)):
        aList[i] = float(aList[i])

def main():
    aList = ["12", "345", "15.34"]

    print("Strings list:", aList)

    toNumbers(aList)

    print("Numbers list:", aList)

main()
