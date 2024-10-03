# Add functionality to an existing function with decorators. 
# This is called metaprogramming.
# A function can take a function as argument (the function to be decorated) and #return the same function with or without extension.
# Extending functionality is very useful at times.

#Functions are first-class objects
print("Ex 1")
def func1():
    print("This is a function")

# I can assign a function to a variable! 
another_func = func1
another_func()
print()
#--------------------------------------------------
print("Ex 2")
# Example of nested functions
# Passing exponents to a number
def outer1(exp):
    def inner(num):
        return num ** exp
    return inner

add_exps = outer1(5)

# the above equals this
# def outer1(5):
#     def inner(num):
#         return num ** 5
#     return inner

result = add_exps(6)
print(result)
print()

#-------------------------------------------------

#-------------------------------------------------
# Basic decorator functionality
print("Ex 3")

def outer(func):
    print("Beginning the outer function")

    # Defining wrapper function
    def wrapper():
        print("Beginning the wrapper function")
        func()
        print("Returning the wrapper function")
    
    # Returning wrapper function
    return wrapper

def basic_func():
    print("I'm just a basic function")

result = outer(basic_func)
result()
print()

#---------------------------------------------------------

#---------------------------------------------------------
# Python decorators are functions that takes in a function and returns it by adding some functionality
print("Ex 4")
def authenticator(func):
    # define inner function
    def wrapper():
        # additional behavior
        print("I'm authenticating a plain ol' django view")
        # call the original function
        func()
    return wrapper

def some_view():
    print("I'm a plain ol' django view")

# Decorating the function by passing the some_view function to the authenticator
# The authenticator returns the wrapper function and assigns it to a variable
result = authenticator(some_view)

# Calling the wrapper function
result()
print()

#-----------------------OR---------------------------------
print("Ex 5")

@authenticator
def some_view():
    print("I'm a plain ol' django view")

some_view()










