/*
Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120f
*/
//recursive
function factorialize(num) {
  if( num == 1){
    return 1;
  }
  else{
    return num*factorialize(num-1);
  }
}

function factorialize2(num){
	var sum = 1;
	for( var i = 1; i <= num; i++){
		sum *= i;
		
	}
	return sum;
}

console.log(factorialize(5));
console.log(factorialize2(5));
