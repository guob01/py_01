import pytest
from utils.read_data import get_data
import allure


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (2, 2, 3) == (2, 2, 3)


@pytest.mark.parametrize("start", get_data()['mobile_params'])
def test_mobile(start):
    print(start)
