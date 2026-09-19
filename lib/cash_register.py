class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Calculate the total price for the item.
        item_total = price * quantity

        # Add the item's total price to the register total.
        self.total += item_total

        # Add the item once for each quantity purchased.
        for _ in range(quantity):
            self.items.append(item)

        # Save the transaction so it can be voided later.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Check whether there is a discount to apply.
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate the discounted total.
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Remove the last transaction after applying the discount.
        self.previous_transactions.pop()

        # Print the updated total.
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        # Do nothing if there are no previous transactions.
        if not self.previous_transactions:
            return

        # Get the most recent transaction.
        transaction = self.previous_transactions.pop()

        # Remove the transaction's cost from the total.
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove each item from the items list.
        for _ in range(transaction["quantity"]):
            self.items.pop()      

