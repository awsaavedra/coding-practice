/*
Truncate a string (first argument) if it is longer than the given 
maximum string length (second argument). 
Return the truncated string with a '...' ending.
*/

function truncate(str, num){
	if( num >= str.length){
		return str;
	}
	var strArr = str.split("");
	//console.log(strArr);
	var arr2 = [];
	for( var i = 0; i < num; i++){
		if( i < num - 3){
			arr2.push(strArr[i]);
		}else{
			arr2.push('.');
		}
	}
	arr2 = arr2.join("");
	//console.log(arr2);
	return arr2;
}

console.log(truncate('A-tisket a-tasket A green and yellow basket', 11));
