def is_right_triangle(a, b, c):
    # first arrange the sides so the biggest one is last
    sides = [a, b, c]
    sides.sort()
    x, y, z = sides

    # right angle triangle rule -> x*x + y*y = z*z
    if x*x + y*y == z*z:
        return True
    else:
        return False


# taking input from user
s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side: "))

result = is_right_triangle(s1, s2, s3)

if result:
    print("Yes, it is a right angle triangle")
else:
    print("No, it is not a right angle triangle")