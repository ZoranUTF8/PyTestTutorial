from typing import List, Dict


class ShoppingCart:

    def __init__(self, max_size: int) -> None:
        self.cartItems: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more item to cart.")
        else:
            self.cartItems.append(item)

    def size(self) -> int:
        return len(self.cartItems)

    def get_items(self) -> List[str]:
        return self.cartItems

    def get_total_price(self, price_map: Dict[str, float]) -> float:
        total_price = 0.0
        for item in self.cartItems:
            total_price += price_map.get(item)

        return total_price
