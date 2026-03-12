classDiagram
direction LR

class Customer {
  +String customerId
  +String fullName
  +String email
  +String phone
  +String defaultAddress
  +List~Transaction~ pastTransactions
}

class MenuItem {
  +String itemId
  +String name
  +String description
  +String category
  +Decimal price
  +Float popularityRating
  +Boolean isAvailable
}

class Menu {
  +String menuId
  +String title
  +Map~String, List~MenuItem~~ categories
}

class Transaction {
  +String transactionId
  +DateTime createdAt
  +List~MenuItem~ items
  +Decimal total
}

Customer "1" --> "0..*" Transaction : has past transactions
Menu "1" o-- "0..*" MenuItem : lists/categorizes
Transaction "1" --> "1..*" MenuItem : contains