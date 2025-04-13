import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution

class CheckoutTest:
    def test_checkout(self):
        assert CheckoutSolution().checkout("ABC")