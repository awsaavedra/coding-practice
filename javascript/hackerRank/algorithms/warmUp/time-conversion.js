/*
	12 hour to military time
		
	hh:mm:ss
*/

function processData(input){
	var arr = input.split("");
	var len = arr.length;
	var outPut = [];
	//hours conversion
	if(arr[len - 2].toLowerCase() == "p"){
		var toMil = Number(arr[0] + arr[1]) + Number(12);
		toMil = String(toMil);	
		var hhArr = toMil.split("");
		arr[0] = hhArr[0];
		arr[1] = hhArr[1];
	}
	if( arr[len - 2].toLowerCase() == "a" && arr[0] == 1 && arr[1] == 2){
		arr[0] = "0";
		arr[1] = "0";
	}


	for( var i = 0; i < len - 2; i++){
		outPut.push(arr[i]);
	}
	//console.log(outPut);

	arr = outPut.join("");

	console.log(arr);
}



console.log(processData("07:05:45PM"));
console.log(processData("12:00:01AM"));
