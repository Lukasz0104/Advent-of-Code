package main

import "fmt"

func main() {
	var s string
	var inp []int
	var i int

	for fmt.Scanln(&s); len(s) > 0; {
		fmt.Sscanf(s, "%d", &i)
		inp = append(inp, i)
		s = ""
		fmt.Scanln(&s)
	}
	part1(&inp)
	part2(&inp)
}

func part1(inp *[]int) {
	//product of two number summing to 2020
	for i1, v1 := range *inp {
		for i2, v2 := range *inp {
			if i1 == i2 {
				continue
			}
			if v1+v2 == 2020 {
				fmt.Println(v1 * v2)
				return
			}
		}
	}
}

func part2(inp *[]int) {
	//product of three numbers summing to 2020
	for i1, v1 := range *inp {
		for i2, v2 := range *inp {
			if i1 == i2 {
				continue
			}
			for i3, v3 := range *inp {
				if i1 == i3 || i2 == i3 {
					continue
				}
				if v1+v2+v3 == 2020 {
					fmt.Println(v1 * v2 * v3)
					return
				}
			}
		}
	}
}
