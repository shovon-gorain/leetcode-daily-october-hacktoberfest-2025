var numWaterBottles = function(numBottles, numExchange) {
    let totalDrank = numBottles;
    let emptyBottles = numBottles;

    while (emptyBottles >= numExchange) {
        let newBottles = Math.floor(emptyBottles / numExchange);
        totalDrank += newBottles;
        emptyBottles = newBottles + (emptyBottles % numExchange);
    }

    return totalDrank;
};
