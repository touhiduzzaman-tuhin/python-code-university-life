class Phone:

    def call(self):

        print("You Can Call")

    def message(self):

        print("You Can Message")


class Nokia:

    def call(self):

        print("You Can Call")

    def message(self):

        print("You Can Message")

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