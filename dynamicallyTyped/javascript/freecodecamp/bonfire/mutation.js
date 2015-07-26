/*
Return true if the string in the first element of the array 
contains all of the letters of the string in the second element of the array.

	assumptions:
		1) array only has 2 elements
		2) arrays elements are strings
*/
//adding contains method to the string prototype
String.prototype.contains = function(it) { 
	return this.indexOf(it) != -1;  
};

function mutation(arr){
	arr[0].sort(function(a, b){
	var nameA=a.name.toLowerCase(), nameB=b.name.toLowerCase();
	if (nameA < nameB) //sort string ascending
		return -1;
	if (nameA > nameB)
		return 1;
	return 0; //default return value (no sorting)
	});
	arr[0] = arr[0].toLowerCase();
	arr[1] = arr[1].toLowerCase();
	if( arr[0].contains(arr[1])){
		return true;
	}else{
		return false;
	}
}

console.log(mutation(['hello', 'hey']));
