class IOSstring() :

    def __init__(self):
        self.str = ""

    def get_string(self) :
        self.str = input("Enter a string")

    def print_string(self) :
        self.str = print(self.str.upper())

str = IOSstring()

str.get_string()
str.print_string()