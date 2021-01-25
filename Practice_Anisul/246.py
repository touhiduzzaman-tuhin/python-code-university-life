class Phone:

    def call(self):

        print("You Can call")

    def message(self):

        print("You Can Message")

class Nokia(Phone):

    def photo(self):

        print("You Can Take Photo")


print(issubclass(Nokia, Phone))
print(issubclass(Phone, Nokia))