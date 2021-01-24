
thisset = {
    "id" : "162-15-7727",
    "name": "Tuhin",
    "cgpa": 3.83
    }

print (thisset)

print (thisset["name"])

print (thisset.get("name"))

thisset["cgpa"] = 3.85

print (thisset)

for x in thisset:
    print (x)

for x in thisset:
    print (thisset[x])

for x in thisset.values():
    print (x)


for x,y in thisset.items():
    print (x,y)

    
if "name" in thisset:
    print ("yes")

print (len (thisset))

thisset["city"] = "Rangpur"

print (thisset)

thisset.pop("id")

print (thisset)


thisset.popitem()

print (thisset)

del thisset["cgpa"]

print (thisset)

thisset.clear()

print (thisset)


thisset = {
    "id" : "162-15-7727",
    "name": "Tuhin",
    "cgpa": 3.83
    }

mylist = thisset.copy()

print (mylist)


mypop = dict(thisset)

print (mypop)


