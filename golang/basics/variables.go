package main
import "fmt"

func main(){

  // var myName string = "Alex S"
  // fmt.Println(len(myName))
  // fmt.Println(myName + " Is a robot!")
  //
  // var isOver20 bool = true
  // fmt.Println("Am I over 20?", isOver20)
  //
  // const pi float64 = 3.14159265
  // fmt.Printf("%.3f \n", pi) //define precision of 3 dec point
  //
  // fmt.Printf("%d \n", 100) //decimal
  // fmt.Printf("%b \n", 100) //binary
  // fmt.Printf("%c \n", 100)
  // fmt.Printf("%x \n", 100)
  // fmt.Printf("%e \n", 100)
  //
    // //logical operators
  // fmt.Println("true && false =", true && false)
  // fmt.Println("true || false =", true || false)
  // fmt.Println("!true =", !true)

    //loops
  // i := 1
  // for i <= 10{
  //   fmt.Println("i = ", i)
  //   i++ // i = i + 1
  // }
  //
  // for j := 0; j < 5; j++{
  //   fmt.Println("j= ",j)
  // }

    //conditionals
  yourAge := 18
  if yourAge >= 16{
    fmt.Println("You Can Drive")
  }else if yourAge >= 18{
    fmt.Println("You can vote")
  }else{
    fmt.Println("You can have fun")
  }

  age := 23
  switch age{
    case 16: fmt.Println("Go drive")
    case 18: fmt.Println("Go vote")
    default: fmt.Println("Go have fun")
  }

}
