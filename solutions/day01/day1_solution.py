class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        """
        Calculates the total number of water bottles you can drink given an initial 
        number of full bottles and a rule for exchanging empty bottles for new full bottles.

        Parameters:
        numBottles (int): Initial number of full water bottles.
        numExchange (int): Number of empty bottles required to exchange for one full bottle.

        Returns:
        int: Total number of water bottles you can drink.
        """

        count = 0          # Total bottles drank so far
        emptyBottles = 0   # Empty bottles we currently have

        while True:
            # Drink all current full bottles
            emptyBottles += numBottles
            count += numBottles

            # Exchange empty bottles for new full bottles
            # divmod returns (quotient, remainder)
            newExchanged, leftovers = divmod(emptyBottles, numExchange)

            # If no new bottles can be exchanged, we are done
            if newExchanged == 0:
                break

            # Update empty bottles for the next iteration
            emptyBottles = leftovers
            # Update number of full bottles to drink next round
            numBottles = newExchanged

        return count
