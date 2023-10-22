from classTut.item import Item


class Phone(Item):
    def __init__(self, id: int, name: str, price: float, qty: int = 0, broken_phones=0) -> None:
        super().__init__(id, name, price, qty)
        assert broken_phones >= 0, "Broken phone phones can't be less than 0"
        self.broken_phones = broken_phones
