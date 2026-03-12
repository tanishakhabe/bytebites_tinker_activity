classDiagram
direction LR

class Customer {
  +String customerId
  +String name
  +List~Transaction~ pastTransactions
}

class Item {
  +String itemId
  +String name
  +Decimal price
  +String category
  +Float popularityRating
}

class Menu {
  +String menuId
  +List~Item~ items
  +getItemsByCategory(category: String) List~Item~
}

class Transaction {
  +String transactionId
  +List~Item~ selectedItems
  +computeTotalCost() Decimal
  +Decimal totalCost
}

Customer "1" --> "0..*" Transaction : has history
Menu "1" o-- "0..*" Item : contains
Transaction "1" --> "1..*" Item : includes