//return the base pair of DNA

function pair(str){
	var arr = [];
	for( var i in str){ //using since creating arrays over and over is getting old
		switch(str[i]){
			case 'A':
				arr.push(['A', 'T']);
				break;
			case 'T':
				arr.push(['T','A']);
				break;
			case 'C':
				arr.push(['C', 'G']);
				break;
			case 'G':
				arr.push(['G', 'C']);	
				break;
		}	
	}
	return arr;
}


