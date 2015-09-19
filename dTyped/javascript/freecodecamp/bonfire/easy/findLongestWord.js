/*
Bonfire: Find the Longest Word in a String
*/

function findLongestWord(str){
	var arr = str.split(' ');
	var l = arr.length;
	var longest = arr[0];
	for( var i = 0; i < l; i++){
		if( arr[i].length > longest.length){
			longest = arr[i];
		} 
	}
	return longest.length;
}

console.log(findLongestWord('The quick brown fox jumped over the lazy dog'));
