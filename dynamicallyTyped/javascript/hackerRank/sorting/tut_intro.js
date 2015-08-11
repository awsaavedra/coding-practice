function processData(input){
	var arr = input.split("\n");
	var arr2 = arr[2].split(" ");
	console.log(arr2.indexOf(arr[0]));
}

processData("4\n6\n1 4 5 7 9 12");

