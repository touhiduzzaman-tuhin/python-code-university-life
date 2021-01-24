div = {
    'Dahaka': 10,
    'Rangpur': 20,
    'Barishal': 15,
    'Khulna': 8,
    'Rajshahi': 12,
    'Chittagang': 8
}

print(div)

div['Khulna'] = 30

print(div)

del div['Dahaka']

print(div)

div['Dahaka'] = 28

print(div)

print(type(div))

print(div['Dahaka'])
print(div['Rajshahi'])
print(div['Khulna'])

div['x'] = 12

print(div)

for i in div:

    print(i)

print(div.keys())

for i in div:

    print(i, div[i])


