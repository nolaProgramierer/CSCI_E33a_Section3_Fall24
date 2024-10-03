# sorted(iterable, key=None, reverse=False)

# iterable: The sequence or collection (e.g., list, tuple, string, etc.) you want to sort.
# key (optional): A function that serves as a custom sorting key. The elements of the iterable are passed through this function to determine their sorting order.
# reverse (optional): A boolean flag to specify if the sorting should be in descending order. By default, it’s False (i.e., ascending order).


nums = (43, 2, 99, 33, -4, 20)

composers = ["Beethoven", "Ravel", "Brahms", "Debussy", "Mahler", "Bruckner", "Mozart", "Bach", "Stravinsky"]

cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]


# Sort these numbers
sorted_nums = sorted(nums)
print(f"1) {sorted_nums}")

print()
# Sort in reverse
rev_sorted_nums = sorted(nums, reverse=True)
print(f"2) {rev_sorted_nums}")

print()
# Sort the composers list by length (ascending)
sorted_by_word_length = sorted(composers, key=len)
print(f"3) {sorted_by_word_length}")

print()
# Sort the cars list by descending price values
sorted_cars = sorted(cars, key=lambda car: car['price'], reverse=True)
print(f"4) {sorted_cars}")

