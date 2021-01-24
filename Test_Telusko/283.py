def Student(name, **data):

    print('Name',name)

    for i in data.values():

        print(i)

Student('Tuhin', age = 25, city = 'Rangpur', mobile = 1764937993)