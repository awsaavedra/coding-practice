/*
You will be provided with an initial array (the first argument 
in the destroyer function), followed by one or more arguments. 
Remove all elements from the initial array that are of the same 
value as these arguments.
*/

function destroyer(arr){
	var newArr = [];
	var len = arr.length;
	for(var i = 0; i < len; i++){
		if( arr[i] !== 2 && arr[i] !== 3){
			newArr.push(arr[i]);
		}
	}
	return newArr;
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));
