class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        total = 10
        start = 9
        current = 9
        while n>1 and start >0:
            current *= start
            total += current
            start -=1
            n -=1
        return total
        