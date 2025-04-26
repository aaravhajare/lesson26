
class Employee() :

    def __init__(self):
        print("employ created")
    
    def __del__(self):
        print("employee deleted")

def create() :
    print("creating employee")
    obj = Employee()
    print("function end")
    del obj

print("creating obj")

create()

print("function end")