/*
array types:
	homogeneous array: array of objects, string, integers, char, etc.
	hetereogenous array: different primitive types mixed or primitives and object, etc.
	
	methods typically used: push, pop, join, splice, sort
		full list: http://www.w3schools.com/js/js_array_methods.asp	
*/

//////////////////////////finishing later\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
var array = [];

//implementing basic array methods, assuming right inputs
var push = function(a){
	array[array.length] = a;
};

var pop = function(){
	var popped = array[array.length-1];
	delete array[array.length-1];
	return popped;
};

var join = function(){
	var result = "";
	array.toString();
}

//testing my methods

//push
console.log("\npush...");
array.push(1);
array.push(2);
console.log(array);

//pop
console.log("\npop...");
console.log(array.pop());
console.log(array);
