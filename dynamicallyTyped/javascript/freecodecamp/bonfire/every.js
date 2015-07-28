//Check if the predicate (second argument) returns truthy (defined) for 
//all elements of a collection (first argument).

function every(collection, pre){
	for( var i in collection){
		if(!collection[i].hasOwnProperty(pre)){
			return false;
		}
	}
	return true;
}
