def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
times3=make_multiplier(3)
print(times3(10))



def multiplier_counter(w,q):
    return w * q
total=multiplier_counter
print(total(3,10))
    

def power_of(n):
    def linner(x):
        return x**n
    return linner



def call_counter():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(f"The function was called{count}times")
    return inner



def my_decorator(func):
    def wrapper():
        print("samething is happening before the function is called")
        func()
        func()
        print("samething is happening hafter the function is called")
    return wrapper
    
def say_whee():
    print("whee") 
say_whee=my_decorator(say_whee)
print(say_whee())     





def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)



def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")




def is_start(func):
    my_dict = {}
    def wrapper(x,y):
        if (x,y) in my_dict:
            print("Already calculated")
            return my_dict[(x,y)]
        else:
            result = func(x,y)
            my_dict[(x,y)] = result
            print(my_dict)
            return result
    return wrapper

@is_start
def add(x,y):
    return x+y
print(add(2,3))
