import datetime

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
    def is_new(self):
        now = datetime.datetime.now()
        date = now.date()
        if date.year - 2 > self.manufacture_date:
            print(f"The piano is new")
        else:
            print("The piano is not new")
        print()


# 1) Let's build three pianos (instances of the class)
p1 = Piano("ebony", 165, 75000, 2018)
p2 = Piano("rosewood", 210, 85000, 2022)
p3 = Piano("white", 285, 285000, 2023)

# 3) Call the 'show' method on 'p1'
p1.show()

# 5) Call the 'is_new' method on 'p2'
p2.is_new()


class Bechstein(Piano):

    def __init__(self, finish, size, price, manufacture_date, line, features=None):
        self.brand = "Bechstein"
        self.line = line
        if features is None:
            features = []
        self.features = features
        super().__init__(finish, size, price, manufacture_date)

     # 7) Write a 'details' (show) method, as in the superclass, for the subclass
    def details(self):
        print(f"This {self.brand} is of the {self.line} line and at ${self.price} is priced accordingly")
        print()

    # 10) Write a method to add features to a subclass instance
    def add_features(self, feature):
        self.features.append(feature)

    # 11) Write a method to return features
    def list_features(self):
        feature_list = []
        for feature in self.features:
            feature_list.append(feature)
        print(feature_list)
        print()


# 6) Instantiate 2 objects of the Bechstein subclass
b1 = Bechstein("walnut", 210, 95000, 2019, "concert")
b2 = Bechstein("ebony", 215, 125000, 1998, "parlor")

# 8) Call the 'details' method on each instance of the subclass
b1.details()
b2.details()

# 9) Call the 'is_new' method of the superclass on the 'b2' instance of the subclass
b2.is_new()

# 12) Add 2 features to the walnut Bechstein
b1.add_features("singing tone")
b1.add_features("warm sound")

# 13) Return the features of the walnut Bechstein
b1.list_features()