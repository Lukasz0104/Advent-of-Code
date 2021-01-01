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
	part2(&inp)
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

func part2(inp *[]int) {
	paths := make(map[int]int)
	paths[(*inp)[len(*inp)-1]] = 1
	for i := len(*inp) - 2; i >= 0; i-- {
		c := 0
		curr := (*inp)[i]
		for j := 1; j < 4; j++ {
			ways, exist := paths[curr+j]
			if exist {
				c += ways
			}
		}
		if c > 0 {
			paths[(*inp)[i]] = c
		}
	}
	ways := paths[0]
	fmt.Println(ways)
}
