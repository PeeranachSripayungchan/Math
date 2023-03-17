def Diamond():
    x = (" ")
    y = ("*")
    try:
        n = int(input("Enter the number: "))
    except ValueError:
        print("Input Can't be Character! Try Again!")
        return Diamond()
    else:
        n = n + 1
        m = 0

        TopAndBottom = (2 * (n - 1) * x) + x
        print(TopAndBottom)
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                if i + j == n:
                    a = x * j
                    b = 2 * y * (i - 1)
                    print("{}{}{}{}".format(a, y, b, a))

        for i in range(0, n, 1):
            for j in range(0, n, 1):
                if i + j == n and i != 1:
                    c = x * i
                    d = 2 * y * (j - 1)
                    print("{}{}{}{}".format(c, y, d, c))
        print(TopAndBottom)

def Rectangle():
    x = ("*")
    try:
        m = int(input("Enter the horizontal: "))
        n = int(input("Enter the vertical: "))
    except ValueError:
        print("Input Can't be Character! Try Again!")
        return Rectangle()
    else:
        for i in range(0, n, 1):
            i = i + 1
            y = m * x
            print("{}{}".format(x, y))

def Triangle():
    x = (" ")
    y = ("*")
    try:
        n = int(input("Enter the number: "))
    except ValueError:
        print("Input Can't be Character! Try Again!")
        return Rectangle()
    else:
        n = n + 1
        m = 0

        TopAndBottom = (2 * (n - 1) * x) + x
        print(TopAndBottom)
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                if i + j == n:
                    a = x * j
                    b = 2 * y * (i - 1)
                    print("{}{}{}{}".format(a, y, b, a))
    
