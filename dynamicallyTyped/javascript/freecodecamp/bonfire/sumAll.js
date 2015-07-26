/*
We'll pass you an array of two numbers. 
Return the sum of those two numbers and all numbers between them.
*/

function sumAll(arr) {
  var sum = 0;
	var a = arr;
	if( a[0] < a[1]){
		for( var i = a[0]; i <= a[1]; i++){
			sum += i;
		}
	}else{
		for( var i = a[1]; i <= a[0]; i++){
			sum += i;
		}
	}
	return sum;
}

console.log(sumAll([1, 4]));

