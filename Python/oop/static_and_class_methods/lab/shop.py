class Shop:
    def __init__(self, name, type_shop, capacity):
        self.name = name
        self.type = type_shop
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type_shop):
        return cls(name, type_shop, capacity=10)

    def add_item(self, item):
        if sum(self.items.values()) >= self.capacity:
            return "Not enough capacity in the shop"

        self.items[item] = self.items.get(item, 0) + 1
        return f"{item} added to the shop"

    def remove_item(self, item, amount):
        product = self.items.get(item)
        if not product or amount > product:
            return f"Cannot remove {amount} {item}"

        self.items[item] -= amount
        if self.items[item] == 0:
            del self.items[item]
        return f"{amount} {item} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
