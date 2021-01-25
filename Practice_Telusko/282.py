def Student(name, **data):

    print('Name',name)

    for i, j in data.items():

        print(i, j)

Student('Tuhin', age = 25, city = 'Rangpur', mobile = 1764937993)