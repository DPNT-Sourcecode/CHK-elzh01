class Deal:
    def __init__(self, amount: int, price: int):
        self.amount = amount
        self.price = price

class Group:
    def __init__(self, deal_amount: int, members: dict[str, int], price: int):
        pairs = sorted([(key, members[key]) for key in members], key = lambda pair: pair[1], reverse=True)
        self.members = [pair[0] for pair in pairs]
        self.deal_amount = deal_amount
        self.price = price

    def consume(self, sku_amounts: dict[str, int]) -> (dict[str, int], int):
        consumed = {}
        consumed_deals = 0
        maybe_consumed = {}
        maybe_amount = 0
        for group_sku in self.members:
            if not group_sku in maybe_consumed:
                maybe_consumed[group_sku] = 0
            if not group_sku in consumed:
                consumed[group_sku] = 0
            if group_sku in sku_amounts:
                amount = sku_amounts[group_sku]
                if amount + maybe_amount < self.deal_amount:
                    maybe_consumed[group_sku] += amount
                    maybe_amount += amount
                else:
                    missing_amount = self.deal_amount - maybe_amount
                    maybe_consumed[group_sku] = missing_amount
                    self._consume_maybe(consumed, maybe_consumed)
                    consumed_deals += 1

                    maybe_amount = amount - missing_amount
                    while maybe_amount >= self.deal_amount:
                        maybe_amount -= self.deal_amount
                        consumed[group_sku] += self.deal_amount
                        consumed_deals += 1
                    maybe_consumed[group_sku] = maybe_amount
        return consumed, consumed_deals

    def _consume_maybe(self, consumed, maybe_consumed):
        for maybe_sku in maybe_consumed:
            consumed[maybe_sku] += maybe_consumed[maybe_sku]
            maybe_consumed[maybe_sku] = 0


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
        "S": {1: 20},
        "T": {1: 20},
        "U": {1: 40},
        "V": {1: 50, 2: 90, 3: 130},
        "W": {1: 20},
        "X": {1: 17},
        "Y": {1: 20},
        "Z": {1: 21},
    }
    GROUPS = [{
        "members": ['S', 'T', 'X', 'Y', 'Z'],
        "amount": 3,
        "price": 45,
    }]

    def __init__(self, price_data: dict[str, dict[int, int]], freebie_data: dict[str, dict[str, int]], group_data: list[dict]):
        self.data: dict[str, list[Deal]] = {}
        self.freebie_data: dict[str, dict[str, int]] = freebie_data
        for sku in price_data:
            sku_data = []
            for amount in price_data[sku]:
                sku_data.append(Deal(amount, price_data[sku][amount]))
            self.data[sku] = sorted(sku_data, key=lambda deal: deal.amount)

            if not len(self.data[sku]) or self.data[sku][0].amount != 1:
                raise ValueError("No deal for single item of sku: {}".format(sku))

        self.groups = [Group(group["amount"], self._augment_group_members(group["members"]), group["price"]) for group in group_data]

    def _augment_group_members(self, members: list[str]):
        augmented_members = {}
        for member in members:
            augmented_members[member] = self.data[member][0].price
        return augmented_members



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




