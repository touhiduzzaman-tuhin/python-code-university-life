class Phone:

    def call(self):

        print("You Can call")

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
n.call()
n.message()
n.photo()