x = 10
def show():
    x = 5
    print("Inside:", x) 
show()
print("Outside:", x)



count = 0
def add():
    global count
    count += 1
    print(count)
    add()


msg="hello yakov"
def outer():
    msg = "Hello"
    def inner():
        global msg
        print(msg)
        inner()
outer()