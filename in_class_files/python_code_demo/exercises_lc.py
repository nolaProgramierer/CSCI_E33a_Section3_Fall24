# List comprehension

 # [expression for item in iterable if condition]
    # 1) expression: expresion to evaluate and append to the new list
    # 2) item: The variable representing each element in the iterable (e.g., a list, tuple, or string).
    # 3) iterable: The sequence or iterable to iterate over
    # 4) condition (optional): An expression to filter elements based on a condition.


# This is a tuple!
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninof", "Chopin", "von Weber"

# Returning a list of composers with the letter 'v' in the name
print("Example")
def v_composers(comp_list):
    new_composers = []
    for composer in comp_list:
        # Filtering with condition
        if "v" in composer:
            new_composers.append(composer)
    print(new_composers)

v_composers(composers)
print()

# list_comp = [expression for item in iterable (if condition == True)]

# 1) Render the above function as a list comprehension


# 2) Render the above function but return the list as lower case