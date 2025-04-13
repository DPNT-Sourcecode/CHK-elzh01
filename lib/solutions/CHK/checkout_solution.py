from .repository import Repository


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        repository = Repository(Repository.PRICE_DEFAULTS, Repository.FREEBIE_DEFAULTS, Repository.GROUPS)
        sku_amounts: dict[str, int] = {}
        sku_freebies: dict[str, int] = {}
        sku_groups: dict[str, int] = {}
        for sku in skus:
            if not sku in sku_amounts:
                sku_amounts[sku] = 0
            sku_amounts[sku] += 1
        for sku in sku_amounts:
            sku_freebies[sku] = repository.check_freebies(sku, sku_amounts)

        price = 0
        for group in repository.groups:
            sku_group, deals = group.consume(sku_amounts)
            price += deals * group.price
            for consumed_sku in sku_group:
                if not consumed_sku in sku_groups:
                    sku_groups[consumed_sku] = 0
                sku_groups[consumed_sku] += sku_group[consumed_sku]

        try:
            for sku in sku_amounts:
                price += repository.price_for(sku, max(0, sku_amounts[sku] - sku_freebies[sku]))
        except:
            return -1
        return price

