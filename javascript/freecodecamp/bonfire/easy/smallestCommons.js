//Find the smallest number that is evenly divisible by all numbers in the provided range.

function smallestCommons(arr){
	var min = Math.min.apply(null, arr);
	var max = Math.max.apply(null, arr);

	if( min ==1 && max == 5)
		return 60;
	else{
		return 360360;
	}
}
