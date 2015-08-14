function processData(input){
	var arr = input.split(/ |\n/);
	arr = arr.slice(1,len);
	var len = arr.length;
	var v = arr[len - 1]; //to be inserted
	for( var i = len - 1; i >= 0; i--){
		if( arr[i - 1] > v){
			var tmp = v;
			arr[i] = arr[i -1];
			var str = arr.join(" ");	
			console.log(str);
			arr[i - 1] = tmp;

		}
	}
	var str = arr.join(" ");
	console.log(str);
}
processData("5\n2 4 6 8 3");
