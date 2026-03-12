name = 'tilak'
newname = ""
for i in name:
    if i not in newname:
        newname += i

data = ['a', 'e', 'i', 'o', 'u']
vowel = 0
cons = 0

for i in newname:
    if i in data:
        vowel = vowel + 1
    else:
        cons = cons + 1

print("vowel = ", vowel)
print("consonant = ", cons)
print("Unique name = ", newname)
