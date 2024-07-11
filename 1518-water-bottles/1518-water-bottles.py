class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottle = numBottles
        while numBottles >= numExchange:
            max_bottle += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return max_bottle
        