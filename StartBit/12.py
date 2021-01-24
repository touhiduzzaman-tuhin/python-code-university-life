class Test:

    def __init__(self):

        print("I am a Constructor")

    def fun1(self):

        print("I am a Function")

    def fun2(self):

        print("I am another Function")

t = Test()
t.fun1()

print("---------------------------------------")


class Test:

    def __init__(self):
        print("I am a Constructor")

    def fun1(self):
        print("I am a Function")

    def fun2(self):
        print("I am another Function")


t = Test()
t.fun2()

print("-------------------------------------")

class User:

    name = ''

    email = ''

    password = ''

    login = False

    def __init__(self, name, email, password):

        self.name = name

        self.email = email

        self.password = password


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

            print("Name : ", self.name ,"\n","Email :", self.email)

        else:

            print("User Not Logged in")


u1 = User("Tuhin", "tuhin@gmail.com", "1234")

print("\n")

u1.login()
u1.profile()