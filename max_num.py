a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
if d > max_num:
    max_num = d
if e > max_num:
    max_num = e
print("The maximum value is:", max_num)
