function plusMinus(str){
	var pos = 0;
	var neg = 0;
	var zero = 0;

	var arr = str.split("\n");
	var len = Number(arr[0]);
	var arr2 = arr[1].split(" ");
	for( var i = 1; i < arr2.length; i++){
		if( Number(arr2[i]) > 0){
			pos += 1;
		}else if( Number(arr2[i]) == 0){
			zero += 1;
		}else if( Number(arr2[i]) < 0){
			neg += 1;
		}
	}	
	console.log("pos: " + (pos/len).toFixed(6) + "\nneg: " + (neg/len).toFixed(6) + "\nzero: " + (zero/len).toFixed(6));
}

console.log(plusMinus(" 6\n -4 3 -9 0 4 1"));
