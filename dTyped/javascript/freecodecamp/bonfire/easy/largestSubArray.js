/*
Return an array consisting of the largest number from each provided 
sub-array. For simplicity, the provided array will contain 
exactly 4 sub-arrays.
*/

function largestOfFour(arr) {
	var len = arr.length; //length
	var largestFour = [];
	for( var i = 0; i < len; i++){
		var innerArr = arr[i];
		var innerLen = arr[i].length;
		var subArrMax = [0];
		for( var j = 0; j < innerArr.length; j++){
			if( innerArr[j] > subArrMax[0]){ //update largest 4
				subArrMax[0] = innerArr[j];
			}
		}
		largestFour.push(subArrMax[0]);
		console.log("largest 4: " + largestFour);
	}
	return largestFour;
}

console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], 
[1000, 1001, 857, 1]]));
