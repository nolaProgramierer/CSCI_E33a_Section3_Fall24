import datetime

# Each of our pianos have the following characteristics:
# 1) finish
# 2) size
# 3) price
# 4) the date it was made

# Here's the class (blueprint)

class Piano:
    def __init__(self, finish, size, price, manufacture_date):
        self.finish = finish
        # size in cms
        self.size = size
        # price in US $
        self.price = price
        self.manufacture_date = manufacture_date

    # 2) Build a method called 'show' to display an instance finish, size and height
    def show(self):
        print(f"This piano has a {self.finish}, is {self.size} in length and costs ${self.price} US")
        print()

    # 4) Build a method call 'is_new' which determines if a piano has been manufactured within the past 2 years  (In other words, is it new)
    

   
# 1) Instantiate 3 instances of the class
p1 = Piano("ebony", 165, 75000, 2018)
p2 = Piano("rosewood", 210, 85000, 2022)
p3 = Piano("white", 285, 285000, 2023)


# 3) Call the 'show' method on 'p1'
p1.show()

# 5) Call the 'is_new' method on 'p2'     

#--------------------------------------------------------------
print()
print()
# Here is a sub class of the Piano class which inherits all the
# Piano class instance variables and method, plus adds more 
# functionality without duplicating code from the superclass (Piano)
#--------------------------------------------------------------
class Bechstein(Piano):

    def __init__(self, finish, size, price, manufacture_date, line, features=None):
        super().__init__(finish, size, price, manufacture_date)
        self.brand = "Bechstein"
        self.line = line
        if features is None:
            features = []
        self.features = features
       
    # 7) Write a 'details' (show) method, as in the superclass, for the subclass

    # 10) Write a method to add features

    # 11) Write a method to return features


# 6) Instantiate 2 objects of the Bechstein subclass


# 8) Call the 'details' method on each instance of the subclass


# 9) Find out if the ebony Bechstein is new, using the method of the superclass


# 12) Add 2 features to the walnut Bechstein


# 13) Return the features of the walnut Bechstein
