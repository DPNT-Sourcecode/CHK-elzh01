from lib.solutions.CHK.repository import Repository


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        repository = Repository(Repository.DEFAULTS)
        sku_amounts = {}
        for sku in skus:
            if not sku in sku_amounts:
                sku_amounts[sku] = 0
            sku_amounts[sku] += 1
        price = 0
        try:
            for sku in sku_amounts:
                price += repository.price_for(sku, sku_amounts[sku])
        except:
            return -1
        return price




