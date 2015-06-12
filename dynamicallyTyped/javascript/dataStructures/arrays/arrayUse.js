/*
stackoverflow: http://stackoverflow.com/questions/11514308/big-o-of-javascript-arrays
COMPLETE ARRAY REFERENCE: http://www.w3schools.com/jsref/jsref_obj_array.asp
	background: Javascript arrays are actually objects (pretty much like 
		everything	else). values, indices, are stored in a hashtable.

	Methods time complexity:
		Access- O(1)
		Appending - O(1), resizing the hashtable is required sometimes O(???)
		Prepending - O(n), using unshift which requires you to move all indices
		insertion - O(1) if the value doesn't exist & O(n) if you shift existing
								values (using splice method or some other means).
		Deletion - O(1) for merely removing a value (popping off), O(n) for
							 reassigning indices (via splice).
		swapping - O(1)

		conclusion: setting and unsetting values = O(1), renumbering/reassigning
			will be O(n).
*/

var array = [];

for( var i = 0; i < 11; i++){
	array.push(i);
} //O(n) since there are 11 elements pushed

console.log("array: " + array);

array.shift();
console.log("array after shifting: " + array);

array.unshift(0);
console.log("array after unshifting: " + array);

console.log("array 0 element: "+ array[0]);

delete array[0];
console.log("array after deleting 2nd element: "+ array);

array.splice(11,12,11,12); //add
console.log("used splice to add elements: " + array);

array.splice(11,12) //remove elements
console.log("used splice to remove same elements: " + array);

array = [5,2,1,4,6,8];
console.log("unsorted array: " + array);
console.log("sorted array using .sort method: " + array.sort());

console.log("reversing array: " + array.reverse());

var array2 = [100,110,120,130];
var joinedAr = array.concat(array2);
console.log("joining arrays using .concat() method: "+  joinedAr);

console.log("sliced array of .joined: " + joinedAr.slice(0,5));

var sentence = "Furious cats attacked the bed";
console.log( "Splitting a sentence into array of strings: " + sentence.split(" "));

console.log("\n Arrays are objects, here is an example: " );
var anArray = [1,2,3,4,5];
console.log("AnArray = " + anArray);
var anotherArray = anArray;
console.log("assigning anotherArray = anArray :" + anotherArray);
anArray = ["a","b","c"];
console.log("after changing anArray it equals: " + anArray + "\n anotherArray = " + anArray);
console.log("why? because anotherArray is referencing the same object as anArray");
console.log("This is a shallow copy");

var names = ["David", "Cynthia", "Raymond", "Clayton", "Jennifer"];

console.log("find index of Raymond: " + names.indexOf("Raymond"));
console.log("note: .indexOf() will return the first index of the val or -1 if not found");
