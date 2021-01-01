package main

import "fmt"

func main() {
	var inp []string
	s := ""
	fmt.Scanln(&s)
	for len(s) > 0 {
		inp = append(inp, s)
		s = ""
		fmt.Scanln(&s)
	}
	moves1 := [2]int{3, 1}
	moves2 := [5][2]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}
	part1(&inp, moves1)
	part2(&inp, moves2)
}

func count(inp *[]string, moves [2]int) int {
	count := 0
	pos := 0
	for l := 0; l < len(*inp); l += moves[1] {
		if (*inp)[l][pos%31] == '#' {
			count++
		}
		pos += moves[0]
	}
	return count
}

func part1(inp *[]string, moves [2]int) {
	fmt.Println(count(inp, moves))
}

func part2(inp *[]string, moves [5][2]int) {
	var res int = 1
	for _, v := range moves {
		res *= count(inp, v)
	}
	fmt.Println(res)
}
