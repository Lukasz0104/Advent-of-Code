package main

import (
	"fmt"
	"strings"
)

type bag struct {
	outer string
	inner []string
}

func main() {
	var inp []bag = nil
	s1 := ""
	s2 := ""
	for fmt.Scanf("%s", &s1); len(s1) > 0; {
		S := s1 + " "
		fmt.Scanf("%s", &s1)
		S += s1
		B := bag{S, []string{}}
		S = ""
		for fmt.Scanf("%s", &s2); !strings.Contains(s2, "."); {
			S += s2 + " "
			s2 = ""
			fmt.Scanf("%s", &s2)
		}
		S += s2
		B.inner = process(S)
		inp = append(inp, B)
		s1 = ""
		s2 = ""
		fmt.Scanf("%s", &s1)
	}
	part1(&inp)
}

func part1(inp *[]bag) {
	count := 0
	excluded := []string{}
	checked := []string{}
	countBag(inp, "shiny gold", &count, &excluded, &checked)
}

func part2(inp []bag) {

}

func process(s string) []string {
	s = strings.ReplaceAll(s, " contain ", "")
	s = strings.ReplaceAll(s, "bags", "")
	s = strings.ReplaceAll(s, " bag", "")
	s = strings.ReplaceAll(s, ".", "")
	a := strings.Split(s, ", ")
	if strings.Contains(s, "no other") {
		a = []string{}
	}
	return a
}

func contains(S *[]string, s string) bool {
	for _, v := range *S {
		if s == v {
			return true
		}
	}
	return false
}

func containsAny(S *[]string, s []string) bool {
	for _, v := range s {
		if contains(S, v) {
			return true
		}
	}
	return false
}

func countBag(inp *[]bag, color string, c *int, ex *[]string, ch *[]string) {
	//iterating over input
	for _, v := range *inp {
		if containsAny(v.inner, color)
	}
}
