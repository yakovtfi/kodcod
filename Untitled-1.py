#def greet():
    #username="yakov"
    #return (f"Hello, {username}!")
#print(greet())



counts = {"a":1, "b":2, "c":3}
for k in list (counts):
    if counts[k] % 2 == 1:
        del counts[k]
print(counts)


text = "debugging"
print(text+"!")




nums = [1, 2, 3]
for i in range(0, len(nums)):
    print(nums[i])



config = {"host": "localhost", "port": 5432,"username":"yakov"}
print(config["username"])



age = 12
print(age + 5)



user_input = "12.5"
print(float(user_input))


def ratio(a, b): 
    if b == 0: return "Error: division by zero" 
    return a / b
print(ratio(10, 0))



import json 
print(json.dumps({"ok": True}))



def down(n):
    if n ==0:
        return 0
    return down(n - 1)
print(down(5))


x = 5
while x > 0:
    x-=1
    print(x)


def add_item(item, bucket=None):
     if bucket is None:
         bucket = []
     bucket.append(item)
     return bucket
print(add_item("a"))
print(add_item("b"))




funcs = [] 
for i in range(3):
    funcs.append(lambda i=i: print(i)) 
for f in funcs: 
    f()



items = [1, 2, 3, 4, 5] 
items = [x for x in items if x % 2 != 0] 
print(items)



a = [1, 4, 9]
b = [2, 3, 6, 8]
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged.extend(a[i:])
merged.extend(b[j:])
print(merged)


import logging 
logging.basicConfig(level=logging.DEBUG) 
logging.debug("Start")



j = 0 
for i in range(3): 
    
    j += 1 
print(j)



name = "Avi"
print(f"User: {name}")



data = [10, 20, 30, 40] 
total = 0 
for i in range(len(data)):
    total += data[i]
print("Total:", total)