//Sum all the prime numbers up to and including the provided number.
//TODO: redo this problem, not trivial at all
function sumPrimes(num){
	var sum = 0;
	for( var i = num; i > 1; i--){
		var j = 2;
		while( i % j !== 0){
			j++;
		}
		if( i === j){ //if it is a prime
			sum += i;
		}
	}
	return sum;
}

console.log(sumPrimes(10));
