from classTut.phone import Phone
from classTut.item import Item


def main():
    print("Main function running")
    item1 = Item(1, "laptop", 4932, 2)
    item1.name = "new laptop"
    print(item1.name)


main()
