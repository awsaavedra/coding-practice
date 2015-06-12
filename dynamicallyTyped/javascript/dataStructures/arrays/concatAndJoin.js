/*
array functions:
	concat, splice,
*/

var cisDept = ["Mike", "Clayton", "Terrill", "Danny", "Jennifer"];
console.log("array1: " + cisDept);
var dmpDept = ["Raymond", "Cynthia", "Bryan"];
console.log("array2: " + dmpDept);
var itDiv = cisDept.concat(dmpDept);
console.log("concat of array1 & array2: " + itDiv);

var Array3 = itDiv.splice(3,3); // arguments: starting point of splice, number of elements 
//to take

console.log("\n array3 after itDiv.splice(3,3): " + Array3);
