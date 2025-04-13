import pytest

from lib.solutions.SUM.sum_solution import SumSolution


class TestSum:
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_x_validated_type(self):
        with pytest.raises(TypeError):
            assert SumSolution().compute("1", 2) == 3

    def test_x_validated_lower_bound(self):
        with pytest.raises(TypeError):
            assert SumSolution().compute("1", 2) == 3





