class Repository:
    DEFAULTS = None

    def __init__(self, data):
        self.data = data

    def price_for(self, sku: str, amount: int) -> int:
        if sku not in self.data:
            raise ValueError("Unknown SKU: {}".format(sku))
        sku_data = self.data[sku].copy()
        price = 0
        while amount > 0:
            sku_data
        return price

