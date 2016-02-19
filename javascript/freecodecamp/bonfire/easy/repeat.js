/*
Repeat a given string (first argument) n times (second argument). 
Return an empty string if n is a negative number.
*/

function repeat(str, num){
	if( num >= 1){
		var repeatStr = "";
		for( var i = 0; i < num; i++){
			repeatStr = str + repeatStr;
		}
		return repeatStr;
	}else{
		return "";
	}
}

console.log(repeat('abc', 3));
