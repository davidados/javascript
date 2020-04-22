import sys


noname = "None" 

def hello_world():
    print("Hello, World!")

def hello(name):
       
    if name == noname:
        print("Hello, World!")
    elif len(name) > 0:
        print("Hello, ", name,  "!")
    else:
        print("Hello, World!")

def print_hello():
    hello(name)

print(hello(name))
name= sys
