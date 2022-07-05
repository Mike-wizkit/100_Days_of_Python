number = int(input("Which number do you want to check? "))
dividing = number % 2
if dividing < 1:
    print("This is an even number.")
else:
    print("This is an odd number.")