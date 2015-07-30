/*
Return true if the given string is a palindrome. Otherwise, return false.
*/

function palindrome(str){
	var isPal = false;
	str = str.replace(/[^a-zA-Z]/g, '').toLowerCase(); //regex to sterilize str
	var revS = str.split('').reverse().join(''); 
	if( str === revS){
		isPal = true;
	}	
	return isPal;
}


console.log(palindrome('ball'));
console.log(palindrome('eye'));
console.log(palindrome("A man, a plan, a canal. Panama"));
