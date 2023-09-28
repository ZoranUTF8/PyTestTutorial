import pytest
from shopping_cart import ShoppingCart


@pytest.fixture
def get_initialized_cart():
    return ShoppingCart(2)
