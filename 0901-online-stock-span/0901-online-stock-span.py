class StockSpanner:

    def __init__(self):
        self.st = []
        self.val = []
        self.i = 0

    def next(self, price: int) -> int:
        while self.st and self.val[-1] <= price:
            self.st.pop()
            self.val.pop()

        res = self.i - self.st[-1] if self.st else self.i + 1
        self.st.append(self.i)
        self.val.append(price)
        self.i += 1

        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)