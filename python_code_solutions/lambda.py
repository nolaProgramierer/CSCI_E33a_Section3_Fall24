# A lambda is a small anonymous function.
# It can take any number of arguments, but have only one expression
# Useful whenever you want to create a function that's only a single line
# and you only need to use it for a short period of time

# 'lambda' is a keyword defining the anonymous function
# the argument is the placeholder
# expression is the code you want to execute in the lambda function

#A lambda function is a small anonymous function.

# Use lambda functions with iterables like 'filter' and 'map'

pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}

#----------------------------------------------
print("1)")
def add_ten(num):
    return num + 10
print(add_ten(10))

#-----------------------------------------------
print()
print("2)")
# The argument before the ":" is the argument
# The expression is after the ":"
x = lambda a : a + 10
print(x(10))

#-----------------------------------------------
print()
print("3)")
# Write the above lambda without passing in an argument to the function variable
z = (lambda x: x + 10)(10)
print(z)

#-----------------------------------------------
print()
print("4)")
# Write a lambda which sums 3 arguments
y = lambda a, b, c : a + b + c
print(y(1, 2, 3))

#---------------------------------------------------
print()
print("5)")
# Return a list of expensive pianos (over 94000)
def expensive_piano(list):
    new_list = []
    for piano in list:
        if list[piano] > 94000:
            new_list.append(piano) 
    return new_list
    
result = expensive_piano(pianos)
print(result)

print()
print("6)")
# Using lambda functions
# The arguments are all the piano keys, the lambda checks each value of the
# key to see if it satisfies the filter.
expensive_pianos = list(filter(lambda piano: pianos[piano] > 94000, pianos))
print(expensive_pianos)

# 1) piano.keys() returns a view object that displays a list of all keys in 'pianos'
# 2) 'filter' is a higher-order function taking 2 arguments, a function and an iterable
# 3) 'filter' applies the given function, a lambda, to each element of the iterable
# 4) the lambda takes one argument 'piano', which represents a key of each iterable item
# 5) It checks if 'pianos[piano] is greater than '94000'
# 6) The 'filter' method returns an iterator that contains only the key for which
#    the lambda function returned true.
#-----------------------------------------------------
print()
print("7)")
list1 = ["Neytiri", "Ronal", "Quaritch", "Tonowari", "Spider"]
# Iterating through a list with a conditional the long way
def five_ltr(list):
    n = []
    for i in list:
        if len(i) == 5:
            n.append(i)
    return n

print(five_ltr(list1))

#Using lambda with filter
print()
print("8)")
fiveLtrName = list(filter(lambda a : len(a) == 5, list1))
print(fiveLtrName)

#-----------------------------------------------------------------------
print()
print("9)")
cars1 = {"Ford": 25000, "Chevy": 35000, "Dodge": 37500}

def increase_price(car_list):
    result = []
    for car in car_list:
        new_price = (car_list[car] * .15) + car_list[car]
        result.append(new_price)
    return result
print(increase_price(cars1))

print()
print("10)")
#Using lambda with map, if you want to modify every value in an iterable

newPrice = list(map(lambda k: "${:.2f}".format((cars1[k] * .15) + cars1[k]), cars1))
print(newPrice)

print()
print("11)")
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda x: x[1])  # Sort by the second element of each tuple
print(pairs)
# Output: [(1, 'one'), (3, 'three'), (2, 'two')]
