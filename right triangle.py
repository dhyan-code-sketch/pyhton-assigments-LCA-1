def right_triangle(a, b, c):
    # first arrange the sides so the biggest one is last
    sides = [a, b, c]
    sides.sort()

    # right angle triangle rule -> x*x + y*y = z*z
    if sides[0]**2 +sides[1]**2 == sides[2]**2:
        print("it is a right angeled triangle")
    else:
        print("it is not a right angeled triangle")


# taking input from user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

right_triangle(a, b, c)
