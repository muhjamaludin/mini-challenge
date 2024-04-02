package main

import "fmt"

func main() {
	squareFill()
}

func squareFill() {
	n := 8

	fmt.Println()
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Print("* ")
		}
		fmt.Println()
	}
	fmt.Println()
}
