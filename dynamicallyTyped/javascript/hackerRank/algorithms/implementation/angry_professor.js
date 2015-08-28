//I'll generalize the solution later so it works for the website
function processData(input){
	var arr = input.replace(/\s+/g, '_').split("_");
	//console.log(arr);
	var slice1 = arr.slice(2,6);	
	var slice2 = arr.slice(10,13);
	console.log(classCalled(Number(arr[2]), slice1));
	console.log(classCalled(Number(arr[9]), slice2));	
}

function classCalled(tol, studArr){
	var count = 0;
	var cancelled = "";
	for( var i = 0; i < studArr.length; i++){
		if( Number(studArr[i]) > 0){
			count +=1;
		}
	}
	if( count > tol){
		cancelled = "NO";
	}
	if( count <= tol){
		cancelled = "YES";
	}

	return cancelled;
}
console.log(processData("2\n4 3\n-1 -3 4 2\n4 2\n0 -1 2 1"));
