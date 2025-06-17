x = int(input("Enter a number: "))

if x % 2 == 0 and x % 3 == 0:
    print("x is divisible by both 2 and 3, so it is divisible by 6 also")
elif x % 2 == 0:
    print("x is divisible by 2")
elif x % 3 == 0:
    print("x is divisible by 3")
else:
    print("x is not divisible by 2 or 3.")
