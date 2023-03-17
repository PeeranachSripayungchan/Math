loop = 1

firstlist = [1, 21, 31, 41, 51, 61, 71, 81, 91]
secondlist = [2, 22, 32, 42, 52, 62, 72, 82, 92]
thirdlist = [3, 23, 33, 43, 53, 63, 73, 83, 93]

while loop == 1:
    a = 1
    b = 1
    print("Fibonacci Sequence")
    n = int(input(("Enter the term of number that you want to find Fibonacci: ")))

    for i in range(0, n, 1):
        if i == 0:
            print("The 1st term of Fibonacci is: 0")
        elif i == 1:
            print("The 2nd term of Fibonacci is: 1")
        elif i == 2:
            print("The 3rd term of Fibonacci is: 1")
        elif i < 0:
            print("ERROR")
        else:
            if i % 2 == 1:
                a = a + b
                if i+1 % 100 in firstlist:
                    print("The " + str(i+1) + "st" + " term of Fibonacci is: " + str(a))
                elif i+1 % 100 in secondlist:
                    print("The " + str(i+1) + "nd" + " term of Fibonacci is: " + str(a))
                elif i+1 % 100 in thirdlist:
                    print("The " + str(i+1) + "rd" + " term of Fibonacci is: " + str(a))
                else:
                    print("The " + str(i+1) + "th" + " term of Fibonacci is: " + str(a))
                
            else:
                b = b + a
                if i+1 % 100 in firstlist:
                    print("The " + str(i+1) + "st" + " term of Fibonacci is: " + str(b))
                elif i+1 % 100 in secondlist:
                    print("The " + str(i+1) + "nd" + " term of Fibonacci is: " + str(b))
                elif i+1 % 100 in thirdlist:
                    print("The " + str(i+1) + "rd" + " term of Fibonacci is: " + str(b))
                else:
                    print("The " + str(i+1) + "th" + " term of Fibonacci is: " + str(b))

