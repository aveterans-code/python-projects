#ch6ex12.py
#numlist

def sumList(nums):
    t = 0
    for num in nums:
        t = t + num
    return t

def main():
    print("This program calculates the sum of numbers in a list\n")

    n = eval(input("Enter how long your number list is: "))

    nums = list(range(1,n+1))

    print(f"The sum of the first {n} numbers is {sumList(nums)}")

main()
