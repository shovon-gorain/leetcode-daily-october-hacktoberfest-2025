class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Keep track of total bottles drunk and empty bottles
        total_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            # Exchange numExchange empty bottles for 1 new bottle
            empty -= numExchange  # Remove exchanged empty bottles
            numExchange += 1      # Increase exchange rate
            total_drunk += 1      # Add new bottle to total drunk
            empty += 1            # Add new empty bottle after drinking

        return total_drunk