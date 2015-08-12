//Return the fn of all odd Fibonacci numbers up to and including 
//the passed number if it is a Fibonacci number.
//1, 1, 2, 3, 5, 8, 13, 21, 34
function sumFibs(num) {
  var f1 = 1, f2 = 1, sum = 1, t;
  while (f2 <= num) {
    if (f2 & 1) sum += f2;
    t = f1 + f2;
    f1 = f2;
    f2 = t;
  }
  return sum;
}

console.log(sumFibs(9));
