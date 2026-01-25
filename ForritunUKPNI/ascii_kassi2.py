# n = int(input())
# if n == 0:
#     print(" x")
#     print("x x")
#     print(" x")

# def top_botoom():
#     print((n+1)*" " +"x")

# def lines(string):
#     print(n*" " + string)

# def middle():
#     print("x" + ((n*2)+1)*" " + "x")

# top_botoom()
# lines("/ \\")
# middle()
# lines("\ /")
# top_botoom()

n = int(input())

if n == 0:
    print(" x")
    print("x x")
    print(" x")
else:
    print((n + 1) * " " + "x")

    for i in range(n):
        space = (n - i)
        gap = (i * 2) + 1
        print(space * " " + "/" + gap * " " + "\\")

    print("x" + ((n * 2) + 1) * " " + "x")

    for i in range(n - 1, -1, -1):
        space = (n - i)
        gap = (i * 2) + 1
        print(space * " " + "\\" + gap * " " + "/")

    print((n + 1) * " " + "x")