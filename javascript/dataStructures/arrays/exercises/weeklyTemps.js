/*
Modify the weeklyTemps object in the chapter so that it stores a month’s worth of
data using a two-dimensional array. Create functions to display the monthly aver‐
age, a specific week’s average, and all the weeks’ averages.
*/

function weekTemps() {
	this.dataStore = [];
	this.add = add;
	this.average = average;
}

function add(temp) {
	this.dataStore.push(temp);
}

function average() {
	var total = 0;
	for (var i = 0; i < this.dataStore.length; ++i) {
		total += this.dataStore[i];
	}
	return total / this.dataStore.length;
}

var thisWeek = new weekTemps();
thisWeek.add(52);
thisWeek.add(55);
thisWeek.add(61);
thisWeek.add(65);
thisWeek.add(55);
thisWeek.add(50);
thisWeek.add(52);
thisWeek.add(49);
console.log(thisWeek.average()); // displays 54.875
