def Hello_Decorator(func):
    def wrapper():
        print("Start function")
        func()
        print("End function")
    return wrapper

@Hello_Decorator
def say_hello():
    print("hello world")
say_hello()




import time
def timing_decorator(func):
   def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"Execution time: {end - start:} seconds")
      return result
   return wrapper


@timing_decorator
def slow_function():
 time.sleep(0.005)
slow_function()



def log_args(func):
    def wrapper(*args, **kwargs):
       print(f"Arguments: {args}, {kwargs}")
       return func(*args, **kwargs)
    return wrapper
@log_args
def add(a, b):
 return a + b
add(3, 5)



def to_uppercase(func):
   def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      if isinstance(result, str):
         return result.upper()
      return result
   return wrapper
@to_uppercase
def greet(name):
 return f"Hello {name}"
print(greet("Yaakov"))



def Count_Calls(func):
   count=0
   def wrapper(*args,**kwargs):
      nonlocal count
      count+=1
      print(f"the call:{count}")
      print(count) 
      func(*args,*kwargs)
   return wrapper
@Count_Calls
def hi():
   print("hi")
hi()
hi()
hi() 


def Authentication_Check(func):
    def inner(*args, **kwargs):
        user = kwargs.get('user')
        if user == 'admin':
            return func(*args, **kwargs)
        else:
            print("Access denied. Admins only.")
    return inner
@Authentication_Check
def view_sensitive_data(*args, **kwargs):
    print("Sensitive data accessed.")
view_sensitive_data(user='admin')
view_sensitive_data(user='guest')
      

def Memoization_Decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
            print(f"Caching result for {n}")
            print(cache)
        return cache[n]
    return wrapper
@Memoization_Decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
print(fibonacci(10)) 
