# Add functionality to an existing function with decorators. 
# This is called metaprogramming.
# A function can take a function as argument (the function to be decorated) and #return the same function with or without extension.
# Extending functionality is very useful at times, we’ll show real world examples # 3 # later in this article.

#Functions are first-class objects

def func1():
    print("This is a function")

# I can assign a function to a variable! 
another_func = func1
another_func()
#--------------------------------------------------

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

#-------------------------------------------------

# Example of passing a function as an argument
def add(x , y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate(func, a, b):
    return func(a, b)

result_add = calculate(add, 2, 3)
print(result_add)

result_subtract = calculate(subtract, 10, 5)
print(result_subtract)

result_multiply = calculate(multiply, 3, 10)
print(result_multiply)

result_divide = calculate(divide, 10, 2)
print(result_divide)

#---------------------------------------------------------
# Basic decorator functionality

def outer(func):
    print("Beginning the outer function")
    def wrapper():
        print("Beginning the wrapper function")
        func()
        print("Returning the wrapper function")
    return wrapper

def basic_func():
    print("I'm just a basic function")

result = outer(basic_func)
result()
#---------------------------------------------------------
# Return function as a return value
# Add a timezone to a greeting

def time_zone(zone):
    def greeting():
        return f" Hello from the {zone} time zone"
    # Returns the inner greeting function
    return greeting

# Here the time_zone function is assigned to the greet variable
hi_there = time_zone("central")
# We need to then call the variable as a function
print(hi_there())

#---------------------------------------------------------
# Python decorators are functions that takes in a function and returns it by adding 
# some functionality

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

#-----------------------OR---------------------------------
print()

@authenticator
def some_view():
    print("I'm a plain ol' django view")

some_view()

#----------------------------------------------------------
# Decorator functions with parameters
#Check whether 2 entries are equal

def str_check(func):
    def inner(n1, n2):
        print("I'm going to check if the names are equal")
        if n1 == n2:
            print("The name must be different")
            return
        print("The names are different")
        return func(n1, n2)
    return inner


# The best way
@str_check
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("glenn", "langdon")

#Verbose way    
# concat_name = str_check(full_name)          
# concat_name("glenn", "laurie")



#----------------------------------------------------------
# DO IN THE PYTHON INTERPRETER
def fave_piano(piano):
    return f"This {piano} is my favorite"

def auditioned_piano(a_function):
    return a_function("Bösendorfer")

auditioned_piano(fave_piano)


def my_name(name):
    return f"My name is {name}"

def your_name(another_name):
    return f"Your name is {another_name}"

def who_is(a_function):
    return a_function("Glenn")

who_is(my_name)
who_is(your_name)






