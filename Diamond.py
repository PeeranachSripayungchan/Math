loop = 1
while loop == 1:

    x = (" ")
    y = ("*")
    n = int(input("Enter the number: "))
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
 
