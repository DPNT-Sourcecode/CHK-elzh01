class Deal:
    def __init__(self, amount: int, price: int):
        self.amount = amount
        self.price = price


class Repository:
    FREEBIE_DEFAULTS = {
        "B": {"E": 2},
        "F": {"F": 3},
        "M": {"N": 3},
        "Q": {"R": 3},
        "U": {"U": 4},
    }
    PRICE_DEFAULTS = {
        "A": {1: 50, 3: 130, 5: 200},
        "B": {1: 30, 2: 45},
        "C": {1: 20},
        "D": {1: 15},
        "E": {1: 40},
        "F": {1: 10},
        "G": {1: 20},
        "H": {1: 10, 5: 45, 10: 80},
        "I": {1: 35},
        "J": {1: 60},
        "K": {1: 70, 2: 120},
        "L": {1: 90},
        "M": {1: 15},
        "N": {1: 40},
        "O": {1: 10},
        "P": {1: 50, 5: 200},
        "Q": {1: 30, 3: 80},
        "R": {1: 50},
        "S": {1: 30},
        "T": {1: 20},
        "U": {1: 40},
        "V": {1: 50, 2: 90, 3: 130},
        "W": {1: 20},
        "X": {1: 90},
        "Y": {1: 10},
        "Z": {1: 50},
    }
    GROUPS = [
        ['S', 'T', 'X', 'Y', 'Z']
    ]

    def __init__(self, price_data: dict[str, dict[int, int]], freebie_data: dict[str, dict[str, int]]):
        self.data: dict[str, list[Deal]] = {}
        self.freebie_data: dict[str, dict[str, int]] = freebie_data
        for sku in price_data:
            sku_data = []
            for amount in price_data[sku]:
                sku_data.append(Deal(amount, price_data[sku][amount]))
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

    def check_freebies(self, sku: str, sku_amounts: dict[str, int]) -> int:
        freebies = 0
        if sku in self.freebie_data:
            for required_sku in self.freebie_data[sku]:
                if required_sku in sku_amounts:
                    amount = sku_amounts[required_sku]
                    while amount >= self.freebie_data[sku][required_sku]:
                        amount -= self.freebie_data[sku][required_sku]
                        freebies += 1
        return freebies

