//foreach...how to use it with node???


//every function

function isEven(num){
	return num% 2 == 0;
}

var nums = [2,1,6,4,5];

var even = nums.every(isEven);	//every returns true is true for every element
isItEven(even);
function isItEven(even){
	if(even){
		console.log("all numbers are even");
	}else{
		console.log("not all numbers are even");
	}
}

nums = [2,4,6,8];
console.log("now with nums reassigned to [2,4,6,8]");
isItEven(nums.every(isEven));


/*
The reduce() function, in conjunction with the add() function, 
works from left to right,
computing a running sum of the array elements, like thi
*/
function concat(accumulatedString, item) {
	return accumulatedString + item;
}

var words = ["the ", "quick ","brown ", "fox "];
var sentence = words.reduce(concat);
console.log("example of reduce function: "+ sentence); // displays "the quick brown fox"
