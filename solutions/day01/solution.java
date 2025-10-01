public class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;  // bottles we can drink
        int empty = numBottles;  // bottles that become empty

        while (empty >= numExchange) {
            int newBottles = empty / numExchange;  // exchange empty for full
            total += newBottles;                  // drink them
            empty = empty % numExchange + newBottles; // update empty bottles
        }

        return total;
    }
}
