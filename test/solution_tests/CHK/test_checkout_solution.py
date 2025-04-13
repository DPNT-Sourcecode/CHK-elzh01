import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:
    def test_checkout_singe(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("AB") == 80
        assert checkout.checkout("ABCD") == 115
        assert checkout.checkout("CD") == 35

    def test_checkout_multiple(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("AAAAAA") == 260
        assert checkout.checkout("AAAAA") == 230
        assert checkout.checkout("BB") == 45
        assert checkout.checkout("BBB") == 75
        assert checkout.checkout("BBBB") == 90

    def test_checkout_garbage(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("ABZC") == -1