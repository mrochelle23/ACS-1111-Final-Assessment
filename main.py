class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        order = Order(self.name, self.favorite_drink)
        return order

class Order:
    def __init__(self, person, type):
        self.person = person
        self.type = type

    def to_string(self):
        return f"{self.person} orders: {self.type}"

class CoffeeBar:
    def __init__(self, barista):
        self.orders_list = []
        self.barista = barista

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        for order in self.orders_list:
            print(f"{self.barista} {order.to_string()}")

class Barista(Person):
    def __init__(self, greeting):
        super(Person, self).__init__()
        self.greeting = greeting

# Instances
Amy = Person("Amy", "Coffee")
Bob = Person("Bob", "Tea")
Cat = Person("Cat", "Milk")
Larrys_Coffee = CoffeeBar("Hey dude!")
Kevin = Barista("Hey dude!")
Kevin = CoffeeBar("Hey dude!")

# Calling the my_order function to create an instance of Order for each person and return it
Amy.my_order()
Bob.my_order()
Cat.my_order()

# Calling the process_orders function to add the orders to the orders_list
Larrys_Coffee.place_order(Amy.my_order())
Larrys_Coffee.place_order(Bob.my_order())
Larrys_Coffee.place_order(Cat.my_order())

# Calling the process_orders function to print the orders
Larrys_Coffee.process_orders()