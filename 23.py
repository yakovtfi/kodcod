def division(Height, Width):
    return Height / (Width * 60)
print(division(120, 2))


import math
def area(Radius):
    return math.pi * Radius * Radius
print(area(5))



def print_user_info(name, age):
    print("User full name:", name)
    print("Use Age :", age)

def print_admin_user(name, age):
    print("User admin name:", name)
    print("User Admin Age:", age)



def process_user(*data):
    name = data[0]

    age = data[1]
    print("User:", name)

    if age < 18:

        print("Minor")
    else:

        print("Adult")
        if age >= 65:

            print("Senior")




def Add_calc(num1,num2):
    return num1+num2
print(Add_calc(2,3))