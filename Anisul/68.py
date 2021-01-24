class Phone:

    def __init__(self):

        print("Phone Class")


class Nokia(Phone):

    def __init__(self):

        super().__init__()
        print("Nokia Class")

n = Nokia()

