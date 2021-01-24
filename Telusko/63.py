class Hello:

    def run(self):

        for i in range(5):

            print("Hello")

class Hi:

    def run(self):

        for i in range(5):

            print("Hi")

h1 = Hello()
h2 = Hi()

h1.run()
h2.run()

print("----")

from threading import *

class Hello(Thread):

    def run(self):
        for i in range(50):
            print("Hello")


class Hi(Thread):

    def run(self):
        for i in range(50):
            print("Hi")


h1 = Hello()
h2 = Hi()

h1.start()
h2.start()

print("----")

from time import sleep

from threading import *

class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")

            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")

            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()
h2.start()

print("------")

from time import sleep

from threading import *

class Hello(Thread):

    def run(self):
        for i in range(50):
            print("Hello")

            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(50):
            print("Hi")

            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()

sleep(0.2)

h2.start()

print("------")

from time import sleep

from threading import *

class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")

            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")

            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()
h2.start()

print("Bye")