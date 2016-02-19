function orbitalPeriod(arr) {

  var GM = 398600.4418;
  var earthRadius = 6367.4447;	
	var arrLen = arr.length;

	function totalTime(avgAlt){
		var totalAlt = avgAlt + earthRadius;
		//T(s) = (2 * PI ) * sqrt( a^3 / GM )
		var time = Math.round((2 * Math.PI)*Math.sqrt(Math.pow(totalAlt, 3)/ GM));
		return time;
	}

	for( var i = 0; i < arrLen; i++){
		arr[i] = {
			name: arr[i].name,
			orbitalPeriod: totalTime(arr[i].avgAlt) //calculate OP w/ kepler's eqn
		}; 
	}

	return arr;
}


orbitalPeriod([{name : "sputkin", avgAlt : 35873.5553}]);
