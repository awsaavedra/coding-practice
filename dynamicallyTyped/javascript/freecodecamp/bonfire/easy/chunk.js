/*
Write a function that splits an array (first argument) into 
groups the length of size (second argument) and returns them as a 
multidimensional array.
*/

/*function chunk(arr, size) {
  var len = arr.length;
	var arr2 = [];
	var count = 0;

	if( len % size == 0){
		for( var i = 0; i < len/size; i++){
			var subArr = [];
			for( var j = 0; j < size; j++){
				subArr.push(arr[count]);
				++count;
			}
			console.log(subArr);
			arr2[i] = subArr;
			console.log("array 2 : " + arr2);
		}
	}else{

	}
  return arr;
} */

function chunk(array, length) { 

  var arr2 = [], i = 0, len = array.length; 

  while (i < len) { 
    arr2.push(array.slice(i, i += length)); 
  } 

  return arr2; 
} 

console.log(chunk(['a', 'b', 'c', 'd'], 2));
console.log(chunk([0, 1, 2, 3, 4, 5], 2)); // return 3 subarrays
