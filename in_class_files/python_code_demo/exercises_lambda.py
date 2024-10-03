# Lambda exercises

pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
list1 = [1, 2, 3, 4]

print("Ex 1")
# Write a method to increase an argument by 10
def add_ten(num):
    return num + 10
print(add_ten(10))
print()

print("Ex 2")
# Write the same method as a lambda
x = lambda a : a + 10
print(x(10))
print()

print("Ex 3")
# Write the above lambda without passing in an argument to the function variable

print()
print("Ex 4")
# Write a lambda which sums 3 arguments

print()
print("Ex 5")
# Return a list of pianos priced over 94000
def expensive_piano(list):
    new_list = []
    for piano in list:
        if list[piano] > 94000:
            new_list.append(piano) 
    return new_list
    
result = expensive_piano(pianos)
print(result)

print()
print("Ex 6")
# Write the above function using a lambda (hint: use a lambda in a 'filter' function)


