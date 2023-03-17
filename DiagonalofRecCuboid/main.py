from DiagonalofRectangleFinderforInteger import Rectangle as Rec
from DiagonalofCuboidFinderforInteger import Cuboid as Cuboid
from DiagonalofHypercuboidFinderforInteger import Hypercuboid as HypCubo

loop = 1
while loop == 1:
    print(" \n")
    print("Find The Diagonal \n")
    print("How many dimension you want to select: \n")
    print("2. Ractangle: \n")
    print("3. Cuboid: \n")
    print("4. Hypercuboid: \n")
    print("If you want to exit: \n")
    print("answer: exit \n")
    print(" \n")
    ans = str(input("").lower())

    if ans == '2':
        Rec()
    elif ans == '3':
        Cuboid()
    elif ans == '4':
        HypCubo()
    elif ans == 'exit':
        break
    else:
        print(" \n")
        print("ERROR \n")
        print("only choice is 2, 3, 4 and exit")
        print(" \n")