from Shape import Diamond as Diamond
from Shape import Rectangle as Rec
from Shape import Triangle as Tri

loop = 1
while loop == 1:
    print(" \n")
    print("Choose the shape \n")
    print("1. Diamond: \n")
    print("2. Rectangle: \n")
    print("3. Triangle: \n")
    print("If you want to exit: \n")
    print("answer: exit \n")
    print(" \n")

    ans = str(input("").lower())

    if ans == '1':
        Diamond()
    elif ans == '2':
        Rec()
    elif ans == '3':
        Tri()
    elif ans == 'exit':
        break
    else:
        print(" \n")
        print("ERROR \n")
        print("only choice is 2, 3, 4 and exit")
        print(" \n")