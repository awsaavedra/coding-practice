//Return an English translated sentence of the passed binary string.

function binaryAgent(str){
	var str = str.split(" ");
	var len = str.length;
	var arr = [];
	for( var i = 0; i < len; i++){
		arr.push(String.fromCharCode(parseInt(str[i],2)));
	}
	arr = arr.join('');
	return arr;
}
