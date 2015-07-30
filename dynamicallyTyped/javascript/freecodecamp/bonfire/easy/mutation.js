/*
Return true if the string in the arr1 element of the array 
contains all of the letters of the string in the arr2 element of the array.

	assumptions:
		1) array only has 2 elements
		2) arrays elements are strings
*/
function mutation(arr) {
  var arr1 = arr[0].toLowerCase();
  var arr2 = arr[1].toLowerCase().split("");
	var inWord = true; 
  arr2.forEach(function(letter){
    if (arr1.indexOf(letter) === -1){
			inWord = false;
		}
  });
  return inWord;
}

console.log(mutation(['hello', 'hey']));
