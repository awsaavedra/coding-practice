/*
Create an object that stores individual letters in an array and has a function for
displaying the letters as a single word.
*/

var str = {
	letters: [],

	word: function(){
		return this.letters.join("");
	}
}

str.letters.push("a");
str.letters.push("b");
console.log(str.letters);
console.log(str.word());
