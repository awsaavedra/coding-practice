/*
The Head Librarian at a library wants you to make a program that calculates 
the fine for returning the book after the return date. 
You are given the actual and the expected return dates. Calculate the fine as follows:

	If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
	If the book is returned in the same month as the expected return date, Fine = 15 Hackos × Number of late days
	If the book is not returned in the same month but in the same year as the expected return date, Fine = 500 Hackos × Number of late months
	If the book is not returned in the same year, the fine is fixed at 10000 Hackos.
*/

function processData(input){
	var arr = input.split("\n");
	var actual = arr[0];
	var expected = arr[1]; 

	actual = actual.split("");
	expected = expected.split("");
	var len = actual.length;
	
	if( sameDate(actual, expected)){
		console.log(0);
	}else{
		//not same year
		if( actual[len-1] != expected[len-1] || actual[len-2] != expected[len-2]){
			console.log(10000);
		}	
		//same year, might not be same month or same day
		else{
								
		} 
	}

	console.log(actual[ len - 6] + "blah");

	//console.log( "actual: " + actual + "\n" + "expected: " + expected);
}



function sameDate(actual, expected){
	var match = true;
	for( var i = 0; i < actual.length; i++){
		if( actual[i] != expected[i]){
			match = false;
		}
	}
	return match;
}

console.log(processData("9 6 2015\n6 6 2015"));
//console.log(processData("5 5 2015\n5 5 2015"));
