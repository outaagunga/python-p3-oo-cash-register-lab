class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []  # Added a list to track transactions

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.extend([title] * quantity)
        self.transactions.append((title, item_total, quantity))  # Record the transaction

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) // 100
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            title, item_total, quantity = last_transaction
            self.total -= item_total
            self.items = self.items[:-quantity]  # Remove the items from the list
        else:
            self.total = 0  # Set total to 0 if there are no transactions

# The following block is for testing purposes when this module is run directly.
if __name__ == "__main__":
    register = CashRegister(20)
    print(register.discount)  # Should print 20

    register.add_item("eggs", 0.98)
    print(register.total)  # Should print 0.98

    register.add_item("book", 5.00, 3)
    print(register.total)  # Should print 15.98

    register.apply_discount()  # Should print "After the discount, the total comes to $12.784."
    register.apply_discount()  # Should print "There is no discount to apply."

    register.add_item("Lucky Charms", 4.5)
    register.add_item("Ritz Crackers", 5.0)
    register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
    print(register.total)  # Should print 14.5

    register.void_last_transaction()
    print(register.total)  # Should print 9.5
