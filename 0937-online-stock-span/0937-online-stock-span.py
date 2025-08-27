class StockSpanner:

    def __init__(self):
        self.i = 0
        self.st = []
        self.vals = []

    def next(self, price: int) -> int:
        while self.st and self.vals[-1] <= price:
            self.st.pop()
            self.vals.pop()

        val = self.i - self.st[-1] if self.st else self.i + 1
        self.st.append(self.i)
        self.vals.append(price)
        self.i += 1

        return val

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)