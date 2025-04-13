class Repository:
    DEFAULTS = None

    def __init__(self, data):
        self.data = data

    def price_for(self, sku: str, amount: int) -> int:
        sku_data = self.data[sku]
        price = 0
        while amount > 0:
            pass
        return price
