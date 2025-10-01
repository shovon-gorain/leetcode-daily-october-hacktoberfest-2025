package main

import "fmt"

func numWaterBottles(numBottles int, numExchange int) int {
	total := numBottles
	empty := numBottles

	for empty >= numExchange {
		newBottles := empty / numExchange
		total += newBottles
		empty = empty%numExchange + newBottles
	}

	return total
}

func main() {
	numBottles := 9
	numExchange := 3
	fmt.Println(numWaterBottles(numBottles, numExchange)) // Output: 13
}
