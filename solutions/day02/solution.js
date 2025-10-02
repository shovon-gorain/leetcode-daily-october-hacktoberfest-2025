/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    /**
     * Calculates the maximum number of water bottles you can drink given:
     * - numBottles: initial full bottles
     * - numExchange: empty bottles required for first exchange (increases by 1 after each exchange)
     * 
     * Returns:
     * number: total number of bottles drank
     */
    
    let count = 0;      // Total bottles drank
    let empty = 0;      // Empty bottles we currently have
    
    while (numBottles > 0) {
        // Drink all full bottles
        count += numBottles;
        empty += numBottles;
        numBottles = 0;
        
        // Can we exchange for 1 new bottle?
        if (empty >= numExchange) {
            numBottles = 1;      // Only 1 bottle can be exchanged per operation
            empty -= numExchange;
            numExchange += 1;    // Increment exchange requirement after each operation
        }
    }
    
    return count;
};

// Example usage:
// console.log(maxBottlesDrunk(13, 6));  // Output: 15
// console.log(maxBottlesDrunk(10, 3));  // Output: 13
var maxBottlesDrunk = function(numBottles, numExchange) {
    let full = numBottles;
    let empty = 0;
    let ans = 0;
    let curEx = numExchange;

    while (full > 0) {
        ans += full;
        empty += full;
        full = 0;

        while (empty >= curEx) {
            empty -= curEx;
            full += 1;
            curEx += 1;
        }
    }
    return ans;
};
