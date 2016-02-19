/*
Store a set of words in an array and display the contents both forward 
and backward.
*/

function words(str){
	var array = str.split(" ");
	console.log(array); //forwards

	console.log(array.reverse());
}

words("they all like cheese");
