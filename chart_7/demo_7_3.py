'''
    使用装饰器改进策略模式
        电商促销折扣示例中，定义体有函数名称，best_promotion用来判断折扣幅度最大的列表中也有函数名称。这种重复是个问题，因为新增策略函数后可能会忘记添加。这种失误不会报错，但是会为系统引入不易察觉的缺陷。
'''


__part_name__ = '使用装饰器改进策略模式'


from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:

    def __init__(self, customer: Customer, cart: list, promo=None):
        self.customer = customer
        self.cart = cart
        self.promo = promo

    def total(self)->float:
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promo is None:
            discount = 0
        else:
            discount = self.promo(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


promotions = []


def promotion(func):
    print('Add promotion: %s to promotions' % func.__name__)
    promotions.append(func)
    return func


@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promotion(order):
    return max(promo(order) for promo in promotions)


if __name__ == '__main__':
    joe = Customer('Jone Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)
    ]
    print(Order(ann, cart, best_promotion))
