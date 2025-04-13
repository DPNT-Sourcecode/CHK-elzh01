import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:
    def test_checkout_single(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("AB") == 80
        assert checkout.checkout("ABCD") == 115
        assert checkout.checkout("CD") == 35

    def test_checkout_multiple(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("AAAAAA") == 250
        assert checkout.checkout("AAAAA") == 200
        assert checkout.checkout("AAAA") == 180
        assert checkout.checkout("AAA") == 130
        assert checkout.checkout("BB") == 45
        assert checkout.checkout("BBB") == 75
        assert checkout.checkout("BBBB") == 90

    def test_checkout_freebie(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("EEB") == 80
        assert checkout.checkout("EEBB") == 110
        assert checkout.checkout("EEBBB") == 125

    def test_checkout_freebie_self(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("F") == 10
        assert checkout.checkout("FF") == 20
        assert checkout.checkout("FFF") == 20
        assert checkout.checkout("FFFF") == 30
        assert checkout.checkout("FFFFF") == 40
        assert checkout.checkout("FFFFFF") == 40

    def test_checkout_garbage(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("ABCZ!") == -1

    def test_group_items(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("ST") == 50
        assert checkout.checkout("STZ") == 45
        assert checkout.checkout("STZZ") == 65
        assert checkout.checkout("SATZCZ") == 65 + 50 + 20