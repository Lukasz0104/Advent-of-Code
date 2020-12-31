package main

import (
	"fmt"
	"sort"
)

func main() {
	var inputs []string
	var s string
	fmt.Scanln(&s)
	for len(s) > 0 {
		inputs = append(inputs, s)
		s = ""
		fmt.Scanln(&s)
	}
	//fmt.Println(len(inputs))
	part1(&inputs)
	part2(&inputs)
}

func part1(inp *[]string) {
	max := 0
	for _, val := range *inp {
		a := evaluate(val)
		if a > max {
			max = a
		}
	}
	fmt.Println(max)
}

func part2(inp *[]string) {
	var sortedInput []int
	for _, v := range *inp {
		sortedInput = append(sortedInput, evaluate(v))
	}
	sort.Ints(sortedInput)
	for i := 1; i < len(sortedInput)-1; i++ {
		if sortedInput[i-1]+1 == sortedInput[i] && sortedInput[i+1]-1 == sortedInput[i] {
			continue
		} else {
			fmt.Println(sortedInput[i] + 1)
			break
		}

	}
}

func evaluate(inp string) int {
	mult := 64
	a := 0
	for i := 0; i < 7; i++ {
		if inp[i] == 'B' {
			a = a + mult
		}
		mult /= 2
	}
	a *= 8
	mult = 4
	for i := 7; i < 10; i++ {
		if inp[i] == 'R' {
			a += mult
		}
		mult /= 2
	}
	return a
}
