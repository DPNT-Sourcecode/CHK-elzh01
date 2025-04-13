class Deal:
    def __init__(self, amount: int, price: int):
        self.amount = amount
        self.price = price


class Repository:
    DEFAULTS = None

    def __init__(self, data: dict[str, list[Deal]]):
        self.data = data
        for sku in data:
            deals = data[sku]
            if not len(deals) or deals[0].amount != 1:
                raise ValueError("No deal for single item of sku: {}".format(sku))

    def price_for(self, sku: str, amount: int) -> int:
        if sku not in self.data:
            raise ValueError("Unknown SKU: {}".format(sku))
        sku_data: list[Deal] = self.data[sku].copy()
        price = 0
        while amount > 0 and len(sku_data):
            best = sku_data.pop()
            while best.amount <= amount:
                amount -= best.amount
                price += best.price
        return price



