import csv


class Item:
    discount = 0.2  # discount is a class level attribute
    all = []

    # __init__ is the constructor method in python
    # qty=0 is default value of qty if not passed
    # self is similar to this keyword

    def __init__(self, id: int, name: str, price: float, qty: int = 0) -> None:
        print(f"An instance created: {name}")
        # validation
        assert price >= 0, f"Price {
            price} is not greater than or equal to zero!"
        assert qty >= 0, f"Quantity {
            price} is not greater than or equal to zero!"

        # Assign to self object
        self.id = id
        self.__name = name  # double underscore name is a private class property/attribute
        self.price = price
        self.qty = qty

        # Actions to execute
        self.all.append(name)

    # adding "@property" decorator make this "name" a read only attribute
    @property
    def name(self):
        return self.__name

    # "@name.setter" (setter) allows to assign value to a read only attribute
    @name.setter
    def name(self, value):
        self.__name = value

    def calcualte_total_price(self) -> float:
        return self.price * self.qty

    def apply_discount(self) -> None:
        self.price = self.price * self.discount

    def get_all_items(self) -> list:
        return self.all

    # Class Method
    # "@classmethod" is a decorator
    # "cls" is a class reference passed as first arg
    # Class methods can be called directly from the class name
    @classmethod
    def instantiate_from_csv(cls):
        """ with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader) """

        f = open("item.csv", 'r')
        reader = csv.DictReader(f)
        items = list(reader)

        for item in items:
            Item(
                id=int(item.get("id")),
                name=item.get("name"),
                price=float(item.get("price")),
                qty=int(item.get("qty"))
            )

    # Static method
    # Static methods can called directly from the class name
    # There is no object reference passed as first argument
    @staticmethod
    def is_integer(num) -> bool:
        # we will count out the floats that are point zero
        # ie 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.qty}')"

    """ @property
    def read_only_property(self):
        return "ADC" """
