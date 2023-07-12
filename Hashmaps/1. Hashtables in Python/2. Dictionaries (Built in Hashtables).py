d = {'name': None, 'age': 34, 'gender': 'male'}

print(d['name'])
print(d.items())

for key, value in d.items():
    print(key, value)

d.clear()

print(d.items())
