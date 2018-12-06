# Using Lambda.
fah = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4': 40}
cel = list(map(lambda x: (float(5)/9)*(x-32), fah.values()))

cel_dict = dict(zip(fah.keys(), cel))

print(cel_dict)

# Using dictionary comprehension.
cel_dict = {k: (float(5)/9)*(v-32) for (k, v) in fah.items()}

print(cel_dict)

