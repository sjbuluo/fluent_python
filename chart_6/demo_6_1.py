'''
    重构策略模式
        策略模式:
            定义一系列算法，一一封装，并且可以相互替换。本模式使得算法可以独立于使用者而变化。
        电商领域有个功能明显可以使用策略模式，即根据客户的属性或订单中的商品计算折扣。
        (字典推导可以只生成KEY而不生成VALUE)
'''


from abc import ABC, abstractclassmethod
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractclassmethod
    def discount(self, order):
        '''返回折扣金额(正值)'''


class FidelityPromo(Promotion):
    '''积分为1000或以上的顾客提供5%的折扣'''

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    '''单个商品为20或以上时提供10%折扣'''

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    '''订单中的不同商品达到10个或以上时提供7%的折扣'''

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


if __name__ == '__main__':
    joe = Customer('Jone Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)
    ]
    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))