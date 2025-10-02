class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        Calculates the maximum number of water bottles you can drink given:
        - numBottles: initial full bottles
        - numExchange: empty bottles required for first exchange (increases by 1 after each exchange)

        Returns:
        int: total number of bottles drank
        """

        count = 0       # Total bottles drank
        empty = 0       # Empty bottles we currently have

        while numBottles > 0:
            # Drink all full bottles
            count += numBottles
            empty += numBottles
            numBottles = 0

            # Can we exchange for 1 new bottle?
            if empty >= numExchange:
                numBottles = 1      # Only 1 bottle can be exchanged per operation
                empty -= numExchange
                numExchange += 1    # Increment exchange requirement after each operation

        return count
