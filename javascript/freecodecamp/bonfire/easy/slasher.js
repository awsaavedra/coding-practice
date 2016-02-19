/*
Return the remaining elements of an array after chopping off n elements from the head.

Remember to use RSAP if you get stuck. Try to pair program. Write your own code.
	analysis:
		2 options: either removal or addition (to a new data structure)

		1) removal, time complexity could be higher (lots of elements to remove) 
				but no additional data structure is used (space efficient)
		2) addition, pushing elements to a new data structure with no additional
			elements will be faster in certain instances ( few elements to push)

*/

function slasher(arr, howMany) {
  var len = arr.length;
	if( howMany < 1){
		return arr;
	}else if( howMany > len){
		return [];
	}else{
		for( var i = 0; i < howMany; i++){
			arr.shift();
		}
		return arr;
	}
}
console.log(slasher([1, 2, 3], 0)); // [1, 2, 3]
console.log(slasher([1, 2, 3], 2)); //3
console.log(slasher([1, 2, 3], 9)); //[]
