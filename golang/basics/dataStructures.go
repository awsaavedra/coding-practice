package main
import "fmt"
func main(){
  var favNums2[5] int

  for i := 0; i < 5; i++{
    favNums2[i] = i
  }
  fmt.Println(favNums2)

  favNums3 := [5]float64 { 1, 2, 3, 4, 5}
  fmt.Println(favNums3)
}
