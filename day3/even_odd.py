mylist = [2, 5, 8, 4, 1, 9, 8]
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for i in mylist:
    if i % 2 == 0:
        even_count += 1
        even_sum += i
    else:
        odd_count += 1
        odd_sum += i

print("Even count = ", even_count)
print("Sum of Even = ", even_sum)
print("-" * 15)
print("Odd count = ", odd_count)
print("Sum of Odd = ", odd_sum)
