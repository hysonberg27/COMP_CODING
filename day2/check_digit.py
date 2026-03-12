n = int(input("Enter a digit: "))

if n > 0 and n < 10:
    print("Positive")
elif n < 0 and n > -10:
    print("Negative")
elif n == 0:
    print("Zero")
else:
    print("Not a single digit")
