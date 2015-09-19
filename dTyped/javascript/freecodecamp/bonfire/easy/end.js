//Check if a string (first argument) ends with the given target string 
//(second argument).
//messy solution, but down to O(n) complexity
function end(str, target){
	str = str.replace(/\s/g, ''); //remove spaces from string
	var strArr = str.split("");
	var targetArr = target.split("");
	var lenArr = strArr.length;
	var lenTarget = target.length;
	var j = 0;
	var match = false;
	for( var i = lenArr - lenTarget; i < lenArr; i++){
		if( strArr[i] == targetArr[j]){
			match = true;
			j++;
		}else{
			return false;
			j++;
		}
	}
	return match;
}

console.log(end("Bastian", "n"));
console.log(end('He has to give me a new name', 'name'));
