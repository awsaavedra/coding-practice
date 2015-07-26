//Find the missing letter in the passed letter range and return it.

function fearNotLetter(str){
	var alph = ['a','b','c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o',
	'q','r','s','t','u','v','w','x','y','z'];
	var arr = str.split('');
	var len = str.length;
	var start = alph.indexOf(arr[0]);
	var end = alph.indexOf(arr[len-1]);
	var j = 0;
	var missing = [];
	for( var i = start; i <= end; i++){
		if( arr[j] !== alph[i]){
			missing += alph[i];
			j--;
		}
		j++;
	}
	return missing;
}
console.log(fearNotLetter("abce"));
