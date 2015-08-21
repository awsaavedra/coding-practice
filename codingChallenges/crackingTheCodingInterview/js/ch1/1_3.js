//given two strings, write a method to decide is one is a permutation of the other
//time complexity: O(nlog(n)) since we are usibg quicksort(), sort()
//space complexity: O(n) since we are creating 2 array data structures,
	//note: I could create a custom string sort function, but space complexity 
	//isn't typically a major concern during interviews
function isPerm(str1, str2){
	if( typeof str1 !== "string" || typeof str2 !== "string")
		return false;
	if( str1.length != str2.length){
		return false;
	}
	str1.toLowerCase();
	str2.toLowerCase();
	str1 = str1.split("");
	str2 = str2.split("");
	str1.sort();
	str2.sort();
	for(var i = 0; i < str1.length; i++){
		if( str1[i] !== str2[i]){
			return false;
		}
	}
	return true;
}
console.log("Is it a string being inputted? " + isPerm(124,152));
console.log(isPerm("edfg", "ffae"));
console.log(isPerm("abcd","abdc"));
