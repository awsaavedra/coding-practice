/*Remove all falsey values from an array.
Falsey values in javascript are false, null, 0, "", undefined, and NaN.
*/

function bouncer(arr) {
	var len = arr.length;
  var newArr = [];
	for( var i = 0; i < len; i++){
		if( arr[i]){
			newArr.push(arr[i]);
		}
	}
  return newArr;
}

console.log(bouncer([7, 'ate', '', false, 9]));
