function isPan(s){
	s = s.toLowerCase();
	var letters = "zqxjkvbpygfwmucldrhsnioate";
	for (var i = 0; i < 26; i++){
		if (s.indexOf(letters.charAt(i)) == -1){
			return false;
		}
	}
	return true;
}

console.log(isPan("this is not a pangram"));
console.log(isPan("The quick brown fox jumps over the lazy dog"));
