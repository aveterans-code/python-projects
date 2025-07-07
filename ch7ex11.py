#ch7ex11.py
    #is leap year?

def isLeap(year):
    if year % 4 != 0:
        return False

    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

def main():
    print("Determines if it is a leap year.\n")

    year = int(input("Enter a year: "))

    if isLeap(year):
        print(year, "is a leap year.")

    else:
        print(year, "is not a leap year.")

if __name__ == '__main__':
    main()
