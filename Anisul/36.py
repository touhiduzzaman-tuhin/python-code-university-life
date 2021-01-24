Student = {
    "101" : "Tuhin",
    "102" : "Rana",
    "103" : "Khan",
    "104" : "Kona",
    "105" : "Shahed",
    "106" : "janu"
}

print(Student)

print(Student["101"])

Student["101"] = "Touhid"

print(Student)

print(Student.get("108", "Not A Valid Key"))

print(Student["100"])