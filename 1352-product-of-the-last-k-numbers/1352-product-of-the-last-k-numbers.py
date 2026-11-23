class ProductOfNumbers:

    def __init__(self):
        self.pre_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_prod = [1]
        else:
            self.pre_prod.append(self.pre_prod[-1] * num)
        

    def getProduct(self, k: int) -> int:
        
        if k >= len(self.pre_prod):
            return 0
        
        return self.pre_prod[-1] // self.pre_prod[len(self.pre_prod) - k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)