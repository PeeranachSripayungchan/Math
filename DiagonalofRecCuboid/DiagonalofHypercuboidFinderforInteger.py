import math

def Hypercuboid():
    print("Find the Diagonal of Hypercuboid/Hypercube (4D-Cuboid/4D-Cube) that is integer") # also can use for diagonal from rectangle or square
    n = int(input("Enter the Max Diagonal number that you want to find: ")) 
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for a in range(0, n, 1):
        a = a + 1
        for b in range(0, n, 1):
            b = b + 1
            for c in range(0, n, 1):
                c = c + 1
                for d in range(0, n, 1):
                    d = d + 1
                    e = math.sqrt(a**2 + b**2 + c**2 + d**2)
                    if e % 10 in list and e <= n:
                        print("All side of Diagonal of Hypercuboid/Hypercube (4D-Cuboid/4D-Cube) that is in integer is: {}, {}, {}, {}, {}".format(a, b, c, d, e))
                    else:
                        pass

    print(" \n")