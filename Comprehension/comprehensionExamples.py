# === Examples of set comprehension ===
# e.g 01
x = set(i * 2 for i in range(4) if i % 2 == 0)
print(x)

# e.g 02
y = set(i for i in (1, 2, 3, 4) if i % 2 == 0)
print(y)

# e.g 03
z = set((a, b) for b in range(3) for a in range (4))
print(z)

# === Examples of dictionary comprehension ===
# e.g 01
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = dict.keys()
values = dict.values()
items = dict.items()
print(keys)
print(values)
print(items)

# e.g 02
dict02 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# For each dict item, multiply each value by 2.
new_dict_values = {k: v*2 for (k, v) in dict02.items()}
print(new_dict_values)

# e.g 03
dict03 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# For each dict item, multiply each key by 2.
new_dict_keys = {k*2: v for (k, v) in dict03.items()}
print(new_dict_keys)
