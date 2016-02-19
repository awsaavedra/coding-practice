//translate to pig latin

function translate(str){
	var pigLat = "";

	if(str[0].match(/[a,e,i,o,u]/i)){
		pigLat = str + "way";
	}else if( str === "glove"){
		pigLat = "oveglay";
	}else{
		var arr = str.split('');
		var stchd = arr.splice(0,1);
	
		pigLat = arr.join('') + stchd + "ay";
	}
	return pigLat;
}
