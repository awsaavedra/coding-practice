function reverseString(str) {
	var arr = str.split("");
	console.log("arr: " + arr);
	
	arr.reverse();

	console.log("reversed array: " + arr);

	arr.join("");

	console.log("stitched :" + arr);
}
console.log(reverseString("Hello"));

