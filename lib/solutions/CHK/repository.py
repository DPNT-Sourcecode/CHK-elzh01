class Deal:
    def __init__(self, amount: int, price: int):
        self.amount = amount
        self.price = price


class Repository:
    DEFAULTS = {
        "A": {1: 50, 3: 130},
        "B": {1: 30, 2: 45},
        "C": {1: 20},
        "D": {1: 15},
    }

    def __init__(self, data: dict[str, dict[int, int]]):
        self.data: dict[str, list[Deal]] = {}
        for sku in data:
            sku_data = []
            for amount in data[sku]:
                sku_data.append(Deal(amount, data[sku][amount]))
            self.data[sku] = sorted(sku_data, key=lambda deal: deal.amount)

            if not len(self.data[sku]) or self.data[sku][0].amount != 1:
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

