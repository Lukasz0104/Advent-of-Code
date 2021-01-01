package main

import (
	"fmt"
	"strings"
)

func main() {
	var inputs []string
	s1 := ""
	fmt.Scanln(&s1)
	s2 := s1
	for len(s1) > 0 {
		s := ""
		s2 = s1
		for len(s2) > 0 {
			s += s2 + ";"
			s2 = ""
			fmt.Scanln(&s2)
		}
		inputs = append(inputs, s)
		s1 = ""
		fmt.Scanln(&s1)
	}
	/*
		for i := range inputs {
			fmt.Println(inputs[i])
		}
	*/
	part1(&inputs)
	part2(&inputs)
}

func part1(inputs *[]string) {
	count := 0
	for _, v0 := range *inputs {
		s := ""
		for _, v1 := range v0 {
			if !strings.Contains(s, string(v1)) && string(v1) != ";" {
				s += string(v1)
			}
		}
		count += len(s)
	}
	fmt.Println(count)
}

func part2(inputs *[]string) {
	count := 0
	for _, v0 := range *inputs {
		split := strings.Split(v0, ";")
		for _, v1 := range split[0] {
			a := true
			for _, v2 := range split[1 : len(split)-1] {
				if !strings.Contains(v2, string(v1)) {
					a = false
					break
				}
			}
			if a {
				count++
			}
		}
	}
	fmt.Println(count)
}
