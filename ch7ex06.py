#ch7ex06.py
#speeding or not

def main():
    print("Speeding fine calculator\n")

    limit = int(input("What is the speed limit? "))
    speed = int(input("Clocked speed? "))

    if speed <= limit:
        print("You are legal!")

    else:
        fine = 50 + 5 * (speed - limit)

        if speed > 90:
            fine = fine + 200
        
        print(f"You messed up. The fine is ${fine:0.2f}")

if __name__ == '__main__':
    main()
