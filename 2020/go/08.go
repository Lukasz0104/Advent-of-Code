package main

import "fmt"

func main() {
	s1 := ""
	s2 := ""
	inputs := []string{}

	for fmt.Scanf("%s %s", &s1, &s2); len(s1) > 0; {
		inputs = append(inputs, (s1 + " " + s2))
		s1 = ""
		s2 = ""
		fmt.Scanf("%s %s", &s1, &s2)
	}
	/*
		for _, v := range inputs {
			fmt.Println(v)
		}
	*/
	part1(&inputs)
	part2(&inputs)
}

func part1(inputs *[]string) {
	count := 0
	visited := []int{}
	for pos := 0; !sliceContains(&visited, pos); {
		visited = append(visited, pos)
		op := ""
		inc := 0
		fmt.Sscanf((*inputs)[pos], "%s%d", &op, &inc)
		switch op {
		case "jmp":
			pos += inc
		case "acc":
			count += inc
			pos++
		default:
			pos++
		}
	}
	fmt.Println(count)
}

func part2(inputs *[]string) {
	count := 0
	//visited := []int{}
	//pos := 0

	fmt.Println(count)
}

func sliceContains(slice *[]int, val int) bool {
	for _, v := range *slice {
		if v == val {
			return true
		}
	}
	return false
}
