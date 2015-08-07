//You are given an array of integers of size N. 
//You need to print the sum of the elements of the array.
function processData(str){
	var re = new RegExp("([0-9]+)/s");
	var arr = str.split(" ");
	var ln = arr[0].split('\n');
	var sum = Number(ln[1]);
	for( var i = 1; i < arr.length; i++){
		sum += Number(arr[i]);
	}
	return sum;
}

