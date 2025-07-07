#ch7ex12.py

from ch7ex11 import isLeap

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isValidDate(month, day, year):
    if 1 <= month <= 12:
        if month != 2:
            lastDay = DAYS_IN_MONTH[month]
        else:
            if isLeap(year):
                lastDay = 29
            else:
                lastDay = 28
        if 1 <= day <= lastDay:
            return True # all good

    return False #either bad month or day of month

def main():
    print("Date Validator\n")


    month, day, year = input("Enter a date (mm/dd/yyy): ").split("/")

    if isValidDate(int(month), int(day), int(year)):
        print("The date is valid.")

    else:
        print("The date is invalid.")

if __name__ == '__main__':
    main()
