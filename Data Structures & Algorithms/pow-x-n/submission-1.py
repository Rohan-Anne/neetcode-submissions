class Solution:
    
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.helper(x, n / 2) ** 2
        else:
            return x * (self.helper(x, (n - 1) / 2) ** 2)

    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n)
        if n < 0:
            return self.helper(1 / x, -1 * n)

        