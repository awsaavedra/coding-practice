/*
	types of mutator functions in an array:
		methods: push, pop, unshift, shift, sort
*/

console.log("already covered push, pop unshift, shift, in arrayUse.js...");

var array = [1,2,3,4,5];

console.log("array.reverse(): " + array.reverse());
console.log("array.sort(): " +array.sort());
console.log("however... sort uses lexigraphic order...");

var newArray = [1,2,3,4,5,515, 540, 100];
console.log("newArray: " + newArray);
console.log("\n for this array .sort doesn't work well..." + newArray.sort());

console.log("You can get it to work using a comparing function to assist it");

function compare(num1, num2) {
	return num1 - num2;
}
newArray.sort(compare);
console.log(newArray);
