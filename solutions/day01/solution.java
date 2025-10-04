class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int sum = (numBottles-1)/(numExchange-1);
        return sum+numBottles;
    }
}


class Solution2 {
    public int numWaterBottles(int numBottles, int numExchange) {
        int count = 0;
        int empty = 0;
        int full = numBottles;

        while (full > 0) {
            // Drink current full bottles
            count += full;
            empty += full;

            // Exchange empty bottles for new full bottles
            full = empty / numExchange;
            empty = empty % numExchange;
        }

        return count;
    }
}