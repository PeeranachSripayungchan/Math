import math

def Rectangle():
    print("Find the Diagonal of Rectangle/Square that is integer") # also can use for diagonal from rectangle or square
    n = int(input("Enter the Max Diagonal number that you want to find: ")) 
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for a in range(0, n, 1):
        a = a + 1
        for b in range(0, n, 1):
            b = b + 1
            c = math.sqrt(a**2 + b**2)
            if c % 10 in list and c <= n:
                print("All side of Diagonal of Rectangle/Square that is in integer is: {}, {}, {}".format(a, b, c))
            else:
                pass

    print(" \n")
    