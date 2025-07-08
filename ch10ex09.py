#ch10ex09.py
#   using a class to calculate volume and surface area of a sphere

import math

class Sphere():
    def __init__(self, radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

    def surfaceArea(self):
        return 4 * math.pi * self._radius ** 2
        
    def volume(self):
        return 4.0/3.0 * math.pi * self._radius ** 3
        
def main():
    print("This program computes the volume and surface area of a sphere\n")
    
    orange = float(input("Enter the radius of the sphere: "))
    nSphere = Sphere(orange)

    print(f"\nSurface area: {nSphere.surfaceArea():0.2f} square units.")
    print(f"Volume: {nSphere.volume():0.2f} cubic units.")

if __name__ == '__main__':
    main()
