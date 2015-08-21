//"""Replace all spaces in a word with `%20`."""
//note: replace() method is optimized for this case...but for an interview...
// assumed string input so I don't have to write all the gotcha conditionals
	//Time complexity: O(n)
	//Space complexity: O(n)
function replaceSpaces(str){
	str = str.split("");
	for(var i = 0; i < str.length; i++){
		if( str[i] === " "){
			str[i] = '%20';
		}
	}
	str = str.join("");
	console.log(str); //return str;
}

replaceSpaces("This is a string");
