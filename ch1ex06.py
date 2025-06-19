#King_ch1ex06.py CIS 110 Feb/1/2024
#modify chaos program 3 by 100


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = x
    z = x
    for i in range( 100 ):
        x = 3.9 * x * ( 1 - x )
        y = 3.9 * ( y - y * y )
        z = 3.9 * z - 3.9 * z * z
        print( x, y, z )
main()
