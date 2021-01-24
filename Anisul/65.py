class Phone:

    def call(self):

        print("You Can Call")

    def message(self):

        print("You Can Message")

class Nokia(Phone):

    def photo(self):

        print("You Can Take Photo")


p = Phone()
p.call()
p.message()

print("\n")

n = Nokia()
n.message()
n.call()
n.photo()

print(issubclass(Nokia, Phone))

print(issubclass(Phone, Nokia))


# Here Nokia == sub-class, child-class, derive-class
# Phone == super-class, parent-class, base-class
