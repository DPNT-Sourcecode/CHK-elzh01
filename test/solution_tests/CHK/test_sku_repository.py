import pytest

from lib.solutions.CHK.repository import Repository


class TestRepository:
    TEST_DATA = {'A': {1: 2, 3: 5}, 'B': {1: 6}}

    def test_single_sku(self):
        repository = Repository(TestRepository.TEST_DATA)
        assert repository.price_for('A', 1) == 2
        assert repository.price_for('B', 1) == 6

    def test_multiple_sku(self):
        repository = Repository(TestRepository.TEST_DATA)
        assert repository.price_for('A', 4) == 7
        assert repository.price_for('B', 4) == 24

    def test_sku_validated(self):
        repository = Repository(TestRepository.TEST_DATA)
        with pytest.raises(ValueError):
            assert repository.price_for('C', 4) == 9

