/*
Write a function that takes two or more arrays and 
returns a new array of unique values in the order of the 
original provided arrays.
	TODO: optimize for time complexity and analyze
*/
//time complexity: O(n^2), could optimize more, but didn't take time
function unite( arr1, arr2, arr3){
		var arr = [];
		var argLen = arguments.length;
		for( var i = 0; i < argLen; i++){
			var arg = arguments[i];

			for( var j = 0; j < arg.length; j++){
				if( arr.indexOf(arg[j]) === -1){
					arr.push(arg[j]);
				}
			}
		}
		return arr;
}

console.log(unite([1, 2, 3], [5, 2, 1, 4], [2, 1]));
