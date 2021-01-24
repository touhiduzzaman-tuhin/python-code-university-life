dic = {

    "name" : "Tuhin",
    "id" : "162-15-7727",
    "sec" : "G"
}

print(dic)

print(dic["name"])
print(dic["id"])

dic["name"] = "shahed"

print(dic)

print(dic.get("name"))

for i in dic:

    print(i, dic[i])

for i in dic.values():

    print(i)

for i in dic.items():

    print(i)

for i, j in dic.items():

    print(i, j)

del dic["name"]

print(dic)