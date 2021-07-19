from abc import ABC,abstractmethod
import random

class MagazineV():
    def __init__(self, name, specialization):
        self.name = name
        self.type = specialization

    def show_info(self):
        print(self.name, self.type)

class Vendor(MagazineV):

    def __init__(self, name, sale):
        self.name = name
        self.sale = sale
        self.tread = None

    def greetings(self):
        print("Добрый день. чтобы вы хотели?".format())
        self.show_goods()
        self.tread = input("Что нибудь выбрали?")
        if self.tread in self.sale:
            print(self.tread and self.sale[self.tread])
        else:
            print('Этого товара нет в наличии но мы привезем')

    def show_goods(self):
        print(self.sale)

class Buyer():
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


sale = {"товар 1": 100, "товар2": 150, "товар3": 25}
vendor = Vendor("Bob", sale)

vendor.greetings()