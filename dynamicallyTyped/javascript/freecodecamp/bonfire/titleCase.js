//Return the provided string with the first letter of each word capitalized.
//first solution, n^2 time complexity
function titleCase(str){
	var arr = str.split(' ');
	var arrLen = arr.length;
	var arr2 = [];
	for( var i = 0; i < arrLen; i++){
		var innerArr = arr[i].split('');
		var innerArr2 = [];
		var innerLen = arr[i].length;
		//console.log(innerArr);
		for(var j = 0; j < innerLen; j++){
			if( j == 0){
				innerArr2.push(innerArr[j].charAt(0).toUpperCase()+ innerArr[j].slice(1));
			}else{
				innerArr2.push(innerArr[j].toLowerCase());
			}
		}
		console.log("inner array "+ innerArr2);
		innerArr2 = innerArr2.join('');
		arr2.push(innerArr2);
	}
	arr2 = arr2.join(' ');
	console.log("array 2: " + arr2);
	return arr2;
}

//second solution goal: nlogn time complexity
console.log(titleCase("SHoRt AnD SToUt"));
console.log(titleCase("I'm a little tea pot"));
