# Comprehension

## Set Comprehension
```python
x = set(i * 2 for i in range(4) if i % 2 == 0)
print(x)
```
Returns {0, 4}

## Dictionary Comprehension
For each dict item, multiply each value by 2 :
```python
dict02 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dict_values = {k : v*2 for (k, v) in dict02.items()}
print(new_dict_values)
```
Returns : {'a': 2, 'b': 4, 'c': 6, 'd': 8}

### Nested Dictionary Comprehension
Convert internal dictionaries to float.
```python
dict = {'one': {'a': 10}, 'two': {'b': 20}}
for (external_key, external_value) in dict.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})

dict.update({external_key: external_value})

print(dict)
```
