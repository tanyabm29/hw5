class Coffee:
    def __init__(self, title, country, age):
        self.title = title
        self.country = country
        self.age = 3

    def get_name(self):
        return self.title

    def set_name(self, title):
        self.title = title

    def shop(self):
        return f'Welcome to our store, we sell {self.title} from {self.country} with age {self.age} years'

coffee_1 = Coffee('Jacobs', 'Brazilia', 5)
print(coffee_1.get_name())
coffee_1.set_name('Monarh')
print(coffee_1.country)
print(coffee_1.age)
print(coffee_1.shop())

