//Flatten a nested array. You must account for varying levels of nesting.

function steamroller(arr){
	var arr2 = []; //flattened array

	function stomp(arr){
		arr.forEach(function(item){
			if(Array.isArray(item)){
				return stomp(item);
			}
			arr2.push(item);
		});
		return arr2;
	}
	return stomp(arr);
}
console.log(steamroller([1, [2], [3, [[4]]]]));
