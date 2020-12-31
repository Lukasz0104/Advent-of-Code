package main

import "fmt"

func main() {
	var inp []string
	s1 := ""
	s2 := ""
	s3 := ""
	s := ""
	for fmt.Scanf("%s%s%s", &s1, &s2, &s3); len(s1) > 0; {
		s = s1 + " " + s2 + " " + s3
		inp = append(inp, s)
		s1 = ""
		fmt.Scanf("%s %s %s", &s1, &s2, &s3)
	}
	part1(&inp)
	part2(&inp)
}

func part1(inp *[]string) {
	//number of occurences in between two numbers
	count := 0
	for _, v := range *inp {
		var a, b int
		var c string
		var s string
		fmt.Sscanf(v, "%d-%d %s %s", &a, &b, &c, &s)
		co := countChar(s, c)
		if a <= co && co <= b {
			count++
		}
	}
	fmt.Println(count)
}

func part2(inp *[]string) {
	//exactly one position is given char
	count := 0
	for _, v := range *inp {
		var a int
		var b int
		var s string
		var c string
		fmt.Sscanf(v, "%d-%d %s %s", &a, &b, &c, &s)
		if (s[a-1] == c[0] || s[b-1] == c[0]) && s[a-1] != s[b-1] {
			count++
		}
	}
	fmt.Println(count)
}

func countChar(s string, c string) int {
	count := 0
	for i := 0; i < len(s); i++ {
		if s[i] == c[0] {
			count++
		}
	}
	return count
}
