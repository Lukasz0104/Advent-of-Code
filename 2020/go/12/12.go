package main

import (
	"fmt"
	"strconv"
)

type instruction struct {
	action byte
	value  int
}

func main() {
	inp := []instruction{}
	s := ""
	for fmt.Scanln(&s); len(s) > 0; {
		d, _ := strconv.ParseInt(s[1:], 10, 0)
		inp = append(inp, instruction{s[0], int(d)})
		s = ""
		fmt.Scanln(&s)
	}
	part1(&inp)
	part2(&inp)
}

func part1(inp *[]instruction) {
	position := [2]int{0, 0}
	direction := [2]int{1, 0}

	for _, v := range *inp {
		switch v.action {
		case 'N':
			position[1] += v.value
		case 'S':
			position[1] -= v.value
		case 'E':
			position[0] += v.value
		case 'W':
			position[0] -= v.value
		case 'L':
			direction = rotate(direction, v.value)
		case 'R':
			direction = rotate(direction, -v.value)
		case 'F':
			position[0] += v.value * int(direction[0])
			position[1] += v.value * int(direction[1])
		}
	}

	fmt.Println(abs(position[0]) + abs(position[1]))
}

func part2(inp *[]instruction) {
	waypoint := [2]int{10, 1}
	position := [2]int{0, 0}
	for _, v := range *inp {
		oldW := waypoint
		switch v.action {
		case 'N':
			waypoint[1] += v.value
		case 'S':
			waypoint[1] -= v.value
		case 'E':
			waypoint[0] += v.value
		case 'W':
			waypoint[0] -= v.value
		case 'L':
			waypoint = rotate(waypoint, v.value)
		case 'R':
			waypoint = rotate(waypoint, -v.value)
		case 'F':
			position[0] += v.value * oldW[0]
			position[1] += v.value * oldW[1]
		}
	}

	fmt.Println(abs(position[0]) + abs(position[1]))
}

func rotate(dir [2]int, a int) [2]int {
	return [2]int{dir[0]*cos(a) - dir[1]*sin(a), dir[0]*sin(a) + dir[1]*cos(a)}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func sin(a int) int {
	if a > 0 {
		return ([3]int{1, 0, -1})[a/90-1]
	}
	return -([3]int{1, 0, -1})[-a/90-1]
}

func cos(a int) int {
	if a < 0 {
		a *= -1
	}
	return ([3]int{0, -1, 0})[a/90-1]
}
