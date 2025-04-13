import pytest

from lib.solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self):
       assert HelloSolution().hello("abc") == "Hello, abc!"


    def test_friend_name_validated_type(self):
        with pytest.raises(TypeError):
            assert HelloSolution().hello(123)

    def test_friend_name_validated_type_allow_printable(self):
        class Printable:
            def __str__(self):
                return "xyz"

        assert isinstance(HelloSolution().hello(Printable()), str)