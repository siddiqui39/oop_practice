

fruits = ["apple", "orange", "banana", "coconut"]
print(dir(fruits))
#print(help(fruits))

print(fruits[2])
print(fruits[0:2])
print(fruits[::2])
print(fruits[::-1])
print(len(fruits))
print("apple" in fruits)
fruits[0] = "water melon"
fruits.append("kaki")
print(fruits)
fruits.insert(0, "apple")
print(fruits)
print(fruits.reverse())
print(fruits.index("water melon"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)
