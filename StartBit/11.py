class User:

    name = ''

    email = ''

    password = ''

    login = False

    def login(self):

        email1 = input("Enter Your Email : ")

        password1 = input("Enter Your Password : ")

        if email1 == self.email and password1 == self.password:

            login = True

            print("Login Success Full")

        else:

            print("Login Failed")


    def logout(self):

        login = False

        print("Logged Out")

    def isloggedin(self):

        if self.login:

            return True

        else:

            return False

    def profile(self):

        if self.isloggedin:

            print(self.name ,"\n", self.email)

        else:

            print("User Not Logged in")


u1 = User()
u1.name = "Touhiduzzaman"
u1.email = "touhiduzzamantuhin95@gmail.com"
u1.password = "12345"

u1.login()
u1.profile()