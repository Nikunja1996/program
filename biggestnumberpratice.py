x = int(input("enter the first number:"))
y = int(input("Enter the second number:"))
z = int(input("Enter the third number:"))
if x > y and x > z:
    print("{} is greatest number among all the three numbers . ".format(x))
elif y > z and y > x:
    print("{} is greatest number among all the three numbers.".format(y))
else:
    print("{} is greatest numbers among all the three numbers.".format(z))
