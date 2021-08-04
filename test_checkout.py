import pytest

class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total


# tests -----------------------------------

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_GetCorrecTotalWithMutipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


def test_CanAddDiscount(checkout):
    checkout.addDiscount("a", 3, 2)


def test_CanApplyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2


def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")