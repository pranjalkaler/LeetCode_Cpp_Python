class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cont_days = 1
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            tpl = self.stack.pop()
            cont_days += tpl[1]
        stock = (price, cont_days)
        self.stack.append(stock)
        print(self.stack)
        return cont_days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)