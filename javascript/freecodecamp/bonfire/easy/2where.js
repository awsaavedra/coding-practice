/*
Return the lowest index at which a value (second argument) 
should be inserted into a sorted array (first argument).
*/

function where(arr, num) {
  var len = arr.length;
	for( var i = 0; i < len; i++){
		if( arr[i-1] < num && arr[i] > num){
			arr.splice(i,0, num); //inserted just to test splicing method knowledge
		}
	}
	return arr.indexOf(num);
}

console.log(where([40, 60], 50));
