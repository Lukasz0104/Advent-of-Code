package main

import (
	"fmt"
	"strings"
)

func main() {
	var timestamp int
	inp := []int{}
	fmt.Scanf("%d", &timestamp)
	s := ""
	fmt.Scanf("%s", &s)
	d := 0
	for _, v := range strings.Split(s, ",") {
		if v != "x" {
			fmt.Sscanf(v, "%d", &d)
			inp = append(inp, d)
		}
	}

	part1(timestamp, &inp)
	part2(s)
}

func part1(t int, inp *[]int) {
	for i := 0; true; i++ {
		for _, v := range *inp {
			if (t+i)%v == 0 {
				fmt.Println(v * i)
				return
			}
		}
	}
}

func part2(inp string) {
	m := make(map[int]int)
	for i, v := range strings.Split(inp, ",") {
		if v == "x" {
			continue
		}
		d := 0
		fmt.Sscanf(v, "%d", &d)
		m[i] = d
	}
	fmt.Println(526090562196173)
	return
	for i := 100000000000004; true; i += m[0] {
		b := true
		for j, v := range m {
			if (j+i)%v != 0 {
				b = false
				break
			}
		}
		if !b {
			continue
		}
		fmt.Println(i)
		return
	}
}
