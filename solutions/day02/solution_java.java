class Solution {
    public int maxBottlesDrunk(int numBottles, int x) {
        // ans = total number of bottles drunk, start by drinking all full bottles you have
        int ans = numBottles;  

        // While you have enough empty bottles to exchange for at least 1 new full bottle
        while (numBottles >= x) {
            // Exchange x empty bottles for 1 full bottle.
            // Net effect: you lose (x - 1) empty bottles, since the new full bottle
            // will be drunk and become 1 empty again.
            numBottles -= x - 1;

            // After each exchange, the exchange rate requirement increases by 1
            x++;

            // You got 1 new bottle to drink, so increase total count
            ans++;
        }

        // Return the maximum number of bottles you can drink
        return ans;
    }
}
