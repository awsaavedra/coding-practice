/*
Drop the elements of an array (first argument), starting from the 
front, until the predicate (second argument) returns true.
*/

function drop(arr, func) {
	var arr2 = [];
	for( var i = 0; i < arr.length; i++){
		if( func(arr[i])){
			arr2.push(arr[i]);
		}
	}
	return arr2;
}

console.log(drop([1, 2, 3], function(n) {return n < 3; }));
console.log(drop([1, 2, 3, 4], function(n) {return n >= 3; }));
