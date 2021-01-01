package main

import (
	"fmt"
	"strings"
)

func main() {
	inp := []string{}
	s := ""
	for fmt.Scanln(&s); len(s) > 0; {
		inp = append(inp, s)
		s = ""
		fmt.Scanln(&s)
	}
	//fmt.Println(len(inp))
	part1(&inp)
}

func part1(inp *[]string) {
	count := 0
	cp := *inp
	prev := make([]string, len(*inp))
	for i, v := range cp {
		cp[i] = strings.ReplaceAll(v, "L", "#")
	}
	for !slicesEqual(&cp, &prev) {
		count++
		prev = cp
		for i := 0; i < len(prev); i++ {
			fmt.Println(cp[i])
			for j := 0; j < len(cp[0]); j++ {
				if numberOfOccupied(&cp, i, j) == 0 && cp[i][j] == 'L' {
					prev[i] = strAssign(cp[i], j, '#')
				} else if numberOfOccupied(&cp, i, j) >= 4 && cp[i][j] == '#' {
					cp[i] = strAssign(cp[i], j, 'L')
				}
			}
		}
		fmt.Println()
	}
	for _, v := range cp {
		fmt.Println(v)
	}
	fmt.Println(count)
}

func strAssign(S string, j int, c byte) string {
	s := ""
	for i := 0; i < len(S); i++ {
		if i != j {
			s += string(S[i])
		} else {
			s += string(c)
		}
	}
	return s
}

func slicesEqual(s1, s2 *[]string) bool {
	for i, v := range *s1 {
		if v != (*s2)[i] {
			return false
		}
	}
	return true
}

func numberOfOccupied(S *[]string, i, j int) int {
	c := 0
	if 0 < i && i < len(*S)-1 && 0 < j && j < len((*S)[0])-1 {
		if (*S)[i-1][j] == '#' {
			c++
		}
		if (*S)[i+1][j] == '#' {
			c++
		}
		if (*S)[i][j-1] == '#' {
			c++
		}
		if (*S)[i][j+1] == '#' {
			c++
		}
		if (*S)[i-1][j-1] == '#' {
			c++
		}
		if (*S)[i+1][j+1] == '#' {
			c++
		}
		if (*S)[i+1][j-1] == '#' {
			c++
		}
		if (*S)[i-1][j+1] == '#' {
			c++
		}
	} else if i == 0 {
		if (*S)[i+1][j] == '#' {
			c++
		}
		if j == 0 {
			if (*S)[i][j+1] == '#' {
				c++
			}
			if (*S)[i+1][j+1] == '#' {
				c++
			}
		} else if j == len((*S)[0])-1 {
			if (*S)[i][j-1] == '#' {
				c++
			}
			if (*S)[i+1][j-1] == '#' {
				c++
			}
		} else {
			if (*S)[i+1][j+1] == '#' {
				c++
			}
			if (*S)[i+1][j-1] == '#' {
				c++
			}
			if (*S)[i][j-1] == '#' {
				c++
			}
			if (*S)[i][j+1] == '#' {
				c++
			}
		}
	} else if i == len(*S)-1 {
		if (*S)[i-1][j] == '#' {
			c++
		}
		if j == 0 {
			if (*S)[i][j+1] == '#' {
				c++
			}
			if (*S)[i-1][j+1] == '#' {
				c++
			}
		} else if j == len((*S)[0])-1 {
			if (*S)[i][j-1] == '#' {
				c++
			}
			if (*S)[i-1][j-1] == '#' {
				c++
			}
		} else {
			if (*S)[i-1][j+1] == '#' {
				c++
			}
			if (*S)[i-1][j-1] == '#' {
				c++
			}
			if (*S)[i][j-1] == '#' {
				c++
			}
			if (*S)[i][j+1] == '#' {
				c++
			}
		}
	} else if j == 0 {
		if (*S)[i-1][j] == '#' {
			c++
		}
		if (*S)[i+1][j] == '#' {
			c++
		}
		if (*S)[i-1][j+1] == '#' {
			c++
		}
		if (*S)[i+1][j+1] == '#' {
			c++
		}
		if (*S)[i][j+1] == '#' {
			c++
		}
	} else {
		if (*S)[i-1][j] == '#' {
			c++
		}
		if (*S)[i+1][j] == '#' {
			c++
		}
		if (*S)[i-1][j-1] == '#' {
			c++
		}
		if (*S)[i+1][j-1] == '#' {
			c++
		}
		if (*S)[i][j-1] == '#' {
			c++
		}
	}

	return c
}
