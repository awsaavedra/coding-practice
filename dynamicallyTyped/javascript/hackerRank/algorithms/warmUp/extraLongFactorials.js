//You are given an integer N. Print the factorial of this number.
// 1 <= input <= 100
function processData(input){
	var sum = 1;
	for( var i = 1; i <= input; i++){
		sum *= i;
	}
	console.log(sum);
}

console.log(processData(5)); //need to figure out how to do this in js, 
//ended up using python and importing from the math library
