function reverseString(str) {
	var arr = str.split('');
	var str2 = arr.reverse().join('');
	return str2;
}

console.log(reverseString('hello'));
