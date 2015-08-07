/*
	12 hour to military time
		
	hh:mm:ss
*/

function processData(input){
	var arr = input.split("");
	console.log("array: " + arr);
	var len = arr.length;

	//hours conversion
	if(arr[len-2].toLowerCase() == "p"){
		var toMil = Number(arr[0] + arr[1]) + Number(12);
		toMil = String(toMil);	
		var hhArr = toMil.split("");
		arr[0] = hhArr[0];
		arr[1] = hhArr[1];
	}


	arr = arr.join("");
	console.log(arr);
}



console.log(processData("07:05:45PM"));
