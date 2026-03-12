char = input("Enter any character: ")
ascii_val = ord(char)

if ascii_val >= 65 and ascii_val <= 90:
    print("The entered character is an Upper Case")
elif ascii_val >= 97 and ascii_val <= 122:
    print("The entered character is a Lower Case")
elif ascii_val >= 48 and ascii_val <= 57:
    print("The entered character is a Digit.")
else:
    print("The entered character is a Special Symbol")
