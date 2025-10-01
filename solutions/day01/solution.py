class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0

        while numBottles >= numExchange:
            count = numBottles // numExchange

            ans += numExchange * count
            numBottles -= numExchange * count

            numBottles += count

        return ans + numBottles
