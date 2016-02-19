/*
	Note: time complexity is still n^2, but the goal with the two helper functions
	was to make the code more readable. 
*/

function processData(input) {
	var len = Number(input);
	var j = len;
	for( var i = 1; i < len+1; i++){
		console.log( space(j) + pound(i));
		j--;
	}
} 

function space(n){
	arr = [];

	for(var i = 1; i < n; i++){
		arr.push(" ");
	}
	arr = arr.join("");
	return arr;
}

function pound(n){
	arr = [];

	for(var i = 0; i < n; i++){
		arr.push("#");
	}
	arr = arr.join("");
	return arr;
}

console.log(processData(6));
console.log("\n");
console.log(processData(8));
