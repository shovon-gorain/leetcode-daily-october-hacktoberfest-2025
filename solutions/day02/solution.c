int maxBottlesDrunk(int numBottles, int numExchange) {
    int count = numBottles;
    int empty = numBottles;

    // Instead of simulation which takes n^2, we can just count of full bottles
    while (empty >= numExchange) {
        count++;
        // We subtract 1 from numExchange here because we are gaining 1 full bottles for numExchange empty bottles
        empty -= numExchange - 1;
        numExchange++;
    }

    return count;
}