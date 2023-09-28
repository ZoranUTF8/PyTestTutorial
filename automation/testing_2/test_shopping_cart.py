from unittest.mock import Mock

from cart_item_database_mock import ItemDatabase
import pytest


def test_add(get_initialized_cart):
    get_initialized_cart.add("apple")
    assert get_initialized_cart.size() == 1


def test_size(get_initialized_cart):
    get_initialized_cart.add("apple")
    assert "apple" in get_initialized_cart.get_items()


def test_get_items():
    assert False


def test_cart_overflow(get_initialized_cart):
    with pytest.raises(OverflowError):
        get_initialized_cart.add("apple")
        get_initialized_cart.add("orange")
        get_initialized_cart.add("banana")


def test_get_total_price():
    pass


def test_can_get_total_price(get_initialized_cart):
    get_initialized_cart.add("apple")
    get_initialized_cart.add("orange")

    cart_item_database = ItemDatabase()

    # we can customize the mocking behaviour
    def mock_get_item_request(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    cart_item_database.get = Mock(side_effect=mock_get_item_request)
    assert get_initialized_cart.get_total_price(cart_item_database) == 3.0
