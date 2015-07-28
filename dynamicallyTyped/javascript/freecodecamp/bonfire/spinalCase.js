//Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
function spinalCase(str){
	str = str.replace(/([a-z])([A-Z])/g, '$1-$2');
	
	str = str.replace(/[\s_]/g, '-');
	
	return str.toLowerCase();
}

console.log(spinalCase('This Is Spinal Tap'));
