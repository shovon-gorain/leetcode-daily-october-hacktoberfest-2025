/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    // Total bottles drunk starts as all the initial full bottles
    let ans = numBottles;

    // While you have enough empty bottles to exchange
    while (numBottles >= numExchange) {
        // Exchange: spend numExchange empties to get 1 full bottle.
        // Net effect = lose (numExchange - 1), because the new bottle
        // will be drunk and becomes another empty.
        numBottles -= (numExchange - 1);

        // Each time, the exchange rate requirement increases
        numExchange++;

        // You just drank 1 more bottle
        ans++;
    }

    return ans;
};
