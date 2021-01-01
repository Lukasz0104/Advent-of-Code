package main

import "fmt"

func main() {
	inp := []string{}
	s := ""
	for fmt.Scanln(&s); len(s) > 0; {
		inp = append(inp, s)
		s = ""
		fmt.Scanln(&s)
	}
	fmt.Println(len(inp))
	part1(&inp)
}

func part1(inp *[]string) {
	inpC := make([]string, len(*inp))
	/*
		s:=""
		for i:=0; i<len((*inp)[0]);i++ {
			s+="."
		}
	*/
	copy(inpC, *inp)

	fmt.Println(inpC)
}

func getNumberOfOccupied(S *[]string, i, j int) int {
	c := 0
	if 0 < i && i < len(*S)-1 && 0 < j && j < len((*S)[0])-1 {
		if (*S)[i-1][j] != '#' {
			c++
		}
		if (*S)[i+1][j] != '#' {
			c++
		}
		if (*S)[i][j-1] != '#' {
			c++
		}
		if (*S)[i][j+1] != '#' {
			c++
		}
		if (*S)[i-1][j-1] != '#' {
			c++
		}
		if (*S)[i+1][j+1] != '#' {
			c++
		}
		if (*S)[i+1][j-1] != '#' {
			c++
		}
		if (*S)[i-1][j+1] != '#' {
			c++
		}
	} else if i == 0 {
		if (*S)[i-1][j] != '#' {
			c++
		}
	}

	return c
}
