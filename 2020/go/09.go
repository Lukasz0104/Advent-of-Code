package main

import "fmt"

func main() {
	inputs := []int64{}

	s := ""
	for fmt.Scanln(&s); len(s) > 0; {
		var d int64
		fmt.Sscanf(s, "%d", &d)
		inputs = append(inputs, d)
		s = ""
		fmt.Scanln(&s)
	}
	//fmt.Println(inputs)

	V := part1(&inputs)
	part2(&inputs, V)
}

func part1(inputs *[]int64) int64 {
	L := len(*inputs)
	for i := 25; i < L; i++ {
		found := false
		for i1, v1 := range (*inputs)[i-25 : i] {
			for i2, v2 := range (*inputs)[i-25 : i] {
				if i1 == i2 {
					continue
				}
				if v1+v2 == (*inputs)[i] {
					found = true
					break
				}
			}
			if found {
				break
			}
		}
		if !found {
			fmt.Println((*inputs)[i])
			return (*inputs)[i]
		}
	}
	return 0
}

func part2(inputs *[]int64, V int64) {
	for i := 0; i < len(*inputs); i++ {
		min := (*inputs)[i]
		max := (*inputs)[i]
		for j := i + 1; i < len(*inputs); j++ {
			s := sumI(inputs, i, j)
			if (*inputs)[j] < min {
				min = (*inputs)[j]
			} else if (*inputs)[j] > max {
				max = (*inputs)[j]
			}
			if s == V {
				fmt.Println(min + max)
				return
			} else if s > V {
				break
			}
		}
	}

}

func sumI(values *[]int64, beg int, end int) int64 {
	var sum int64 = 0
	for i := beg; i <= end; i++ {
		sum += (*values)[i]
	}
	return sum
}
