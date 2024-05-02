package src

import "fmt"

func RectangularFill(num int) {
	for i := 0; i < num; i++ {
		for i := 0; i < num; i++ {
			fmt.Printf("* ")
		}
		fmt.Println()
	}
}
