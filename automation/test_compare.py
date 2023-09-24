import pytest


@pytest.mark.skip(reason="HA HA")
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
