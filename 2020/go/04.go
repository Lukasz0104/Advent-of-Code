package main

import (
	"fmt"
	"strings"
)

func main() {
	var inputs []string
	var s1 string = ""
	var s2 string = ""
	fmt.Scanf("%s", &s2)
	s1 = s2
	for len(s1) > 0 {
		var s string = ""
		s2 = s1
		for len(s2) > 0 {
			s += s2 + ";"
			s2 = ""
			fmt.Scanf("%s", &s2)
		}
		inputs = append(inputs, s)
		s1 = ""
		fmt.Scanf("%s", &s1)
	}
	part1(&inputs)
	part2(&inputs)
}

func part1(inputs *[]string) {
	count := 0
	conditions := [7]string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

	for _, val := range *inputs {
		valid := true
		for _, con := range conditions {
			if !strings.Contains(val, con) {
				valid = false
				break
			}
		}
		if !valid {
			continue
		}
		count++
	}
	fmt.Println(count)
}

func part2(inputs *[]string) {
	count := 0
	conditions := [7]string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, v := range *inputs {
		valid := true
		for _, con := range conditions {
			if !strings.Contains(v, con) {
				valid = false
				break
			}
		}
		if !valid {
			continue
		} else {
			split := strings.Split(v, ";")
			m := make(map[string]string)

			for i := 0; i < len(split)-1; i++ {
				t := strings.Split(split[i], ":")
				m[t[0]] = t[1]
			}
			//byr
			byr := 0
			fmt.Sscanf(m["byr"], "%d", &byr)
			if byr < 1920 || byr > 2002 {
				continue
			}
			//iyr
			iyr := 0
			fmt.Sscanf(m["iyr"], "%d", &iyr)
			if iyr < 2010 || iyr > 2020 {
				continue
			}
			//eyr
			eyr := 0
			fmt.Sscanf(m["eyr"], "%d", &eyr)
			if eyr < 2020 || eyr > 2030 {
				continue
			}
			//hgt
			hgt := 0
			if strings.Contains(m["hgt"], "in") {
				fmt.Sscanf(m["hgt"], "%din", &hgt)
				if hgt < 59 || hgt > 76 {
					continue
				}
			} else if strings.Contains(m["hgt"], "cm") {
				fmt.Sscanf(m["hgt"], "%dcm", &hgt)
				if hgt < 150 || hgt > 193 {
					continue
				}
			} else {
				continue
			}
			//hcl
			hcl := ""
			fmt.Sscanf(m["hcl"], "%s", &hcl)
			if len(hcl) < 7 {
				continue
			} else if hcl[0] != '#' {
				continue
			} else {
				for c := range hcl[1:] {
					if !strings.Contains("0123456789abcdef", string(hcl[c])) {
						continue
					}
				}
			}
			//ecl
			ecl := ""
			fmt.Sscanf(m["ecl"], "%s", &ecl)
			if !strings.Contains("amb;blu;brn;gry;grn;hzl;oth", ecl) {
				continue
			}
			//pid
			pidI := 0
			pidS := m["pid"]
			fmt.Sscanf(pidS, "%d", &pidI)
			if len(pidS) != 9 {
				continue
			}
			count++
		}
	}
	fmt.Println(count)
}
