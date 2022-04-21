import random


class Record:
    def __init__(self):
        self.orders = []

    def record(self, order_id):
        self.orders.append(order_id)

    def get_last(self, i):
        return (len(self.orders)-i-1)


if __name__ == "__main__":
    records = Record()
    for i in range(1, 200):
        records.record(i)
    print(records.get_last(44))
