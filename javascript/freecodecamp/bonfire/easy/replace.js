//Perform a search and replace on the sentence using the arguments 
//provided and return the new sentence.

function replace(str, before, after) {
	var arr = str.split(" ");
	console.log( " array: " + arr);
	var len = arr.length;
	for( var i = 0; i < len; i++){
		if( arr[i] == before){
			arr[i] = after;
		}
	}
	var arr2 = arr.join(" ");
	return arr2;
}
console.log(replace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"));
