import pytest

from lib.solutions.CHK.repository import Repository


class TestRepository:
    TEST_PRICE_DATA = {'A': {1: 2, 3: 5}, 'B': {1: 6}, 'C': {1: 7, 2: 10}}
    TEST_FREEBEE_DATA = {'C': {'B': 2}}

    def test_data_validation_no_deals(self):
        with pytest.raises(ValueError):
            repository = Repository({'A': {}}, TestRepository.TEST_FREEBEE_DATA)

    def test_data_validation_no_deal_for_1(self):
        with pytest.raises(ValueError):
            repository = Repository({'A': {2: 2}}, TestRepository.TEST_FREEBEE_DATA)

    def test_single_sku(self):
        repository = Repository(TestRepository.TEST_PRICE_DATA, TestRepository.TEST_FREEBEE_DATA)
        assert repository.price_for('A', 1) == 2
        assert repository.price_for('B', 1) == 6

    def test_multiple_sku(self):
        repository = Repository(TestRepository.TEST_PRICE_DATA, TestRepository.TEST_FREEBEE_DATA)
        assert repository.price_for('A', 4) == 7
        assert repository.price_for('B', 4) == 24

    def test_sku_validated(self):
        repository = Repository(TestRepository.TEST_PRICE_DATA, TestRepository.TEST_FREEBEE_DATA)
        with pytest.raises(ValueError):
            assert repository.price_for('C', 4) == 9

    def test_freebee_amount(self):
        repository = Repository(TestRepository.TEST_PRICE_DATA, TestRepository.TEST_FREEBEE_DATA)
        assert repository.check_freebies('A', {'B': 5}) == 0
        assert repository.check_freebies('C', {'B': 5}) == 2
