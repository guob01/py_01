import pytest
from utils.read_data import read_yaml
import allure


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (2, 2, 3) == (2, 2, 3)


@pytest.mark.parametrize("start", read_yaml()['mobile_params'])
def test_mobile(start):
    print(start)
