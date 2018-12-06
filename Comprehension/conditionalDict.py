# Conditional dictionary comprehension.
# if.
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

new_dict = {k: v for (k, v) in dict.items() if v > 3}
print(new_dict)

# if else.
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_dict = {k: ('even no' if v % 2 == 0 else 'odd no') for (k, v) in dict.items()}
print(new_dict)

# Multiple ifs.
new_dict = {k: v for (k, v) in dict.items() if v > 3 if v % 2 == 0}
print(new_dict)
