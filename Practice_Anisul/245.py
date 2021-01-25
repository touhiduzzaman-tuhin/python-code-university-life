class Phone:

    def call(self):

        print("You Can call P")

    def message(self):

        print("You Can Message P")

class Nokia:

    def call(self):

        print("You Can Call N")

    def message(self):

        print("You Can Message N")

    def photo(self):

        print("You Can Take Photo N")





p = Phone()
p.call()
p.message()



n = Nokia()

p.call()
n.message()
n.photo()