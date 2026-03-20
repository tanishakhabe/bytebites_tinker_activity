from __future__ import annotations

from decimal import Decimal
from typing import List, Optional


class Customer:
    """Represents a user and their purchase history."""

    def __init__(
        self,
        customer_id: str,
        name: str,
        past_transactions: Optional[List["Transaction"]] = None,
    ) -> None:
        self.customer_id = customer_id
        self.name = name
        self.past_transactions = past_transactions or []

    def add_transaction(self, transaction: "Transaction") -> None:
        """Attach a completed transaction to this customer."""
        self.past_transactions.append(transaction)


class Item:
    """Represents a single menu item."""

    def __init__(
        self,
        item_id: str,
        name: str,
        price: Decimal,
        category: str,
        popularity_rating: float,
    ) -> None:
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """Represents the full menu collection."""

    def __init__(self, menu_id: str, items: Optional[List[Item]] = None) -> None:
        self.menu_id = menu_id
        self.items = items or []

    def add_item(self, item: Item) -> None:
        """Add a menu item to this menu."""
        self.items.append(item)

    def get_items_by_category(self, category: str) -> List[Item]:
        """Return items that match the given category."""
        return [item for item in self.items if item.category.lower() == category.lower()]


class Transaction:
    """Represents a customer's selected items and total."""

    def __init__(
        self,
        transaction_id: str,
        selected_items: Optional[List[Item]] = None,
    ) -> None:
        self.transaction_id = transaction_id
        self.selected_items = selected_items or []
        self.total_cost = Decimal("0.00")

    def add_item(self, item: Item) -> None:
        """Add an item to the transaction."""
        self.selected_items.append(item)

    def compute_total_cost(self) -> Decimal:
        """Compute and store the transaction total."""
        self.total_cost = sum((item.price for item in self.selected_items), Decimal("0.00"))
        return self.total_cost