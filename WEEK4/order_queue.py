class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class Icecreamshop:
    def __init__(self, flavours):
        self.flavours = flavours
        self.orders = Queue()

    def take_order(self, customer, flavour, scoops):
        if flavour not in self.flavours:
            print("Flavour does not exist!")
        elif not (1 <= scoops <= 3):
            print("You can only choose 1-3 scoops of ice cream.")
        else:
            print("Order created!")
            order = {"customer": customer, "flavor": flavour, "scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Orders:")
        self.orders.show_queue()

    def next_order(self):
        order = self.orders.dequeue()
        if order:
            print(f"Next Order: Customer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']}")
        else:
            print("No more orders in the queue.")

shop = Icecreamshop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
