from lib.solutions.CHK.repository import Repository


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        repository = Repository(Repository.DEFAULTS)
        sku_amounts = {}
        for sku in 

