package main

import (
	"fmt"
	"sort"
)

func main() {
	inp := []int{0}

	s := ""
	for fmt.Scanln(&s); len(s) > 0; {
		d := 0
		fmt.Sscanf(s, "%d", &d)
		inp = append(inp, d)
		s = ""
		fmt.Scanln(&s)
	}
	part1(&inp)
}

func part1(inp *[]int) {
	sort.Ints(*inp)
	diff1 := 0
	diff3 := 1
	for i := 1; i < len(*inp); i++ {
		if (*inp)[i]-(*inp)[i-1] == 1 {
			diff1++
		} else {
			diff3++
		}
	}
	fmt.Println(diff1 * diff3)
}

func part2() {

}
