import pytest

from lib.solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self):
        hello = HelloSolution()


    def test_friend_name_validated_type(self):
        with pytest.raises(TypeError):
            assert HelloSolution().hello(123)