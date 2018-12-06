# Using a for loop.
dict = {}

for i in range(10):
    if i % 2 == 0:
        dict[i] = i**2

print(dict)

# Using dictionary comprehension.
dict = {i: i**2 for i in range(10) if i % 2 == 0}
print(dict)
