/*
Create a grades object that stores a set of student grades in an object. 
Provide a function for adding a grade and a function for displaying 
the student’s grade average.
*/

var students = {
	var grades = [];

	add: function(grade){
		this.grades.push(grade);
		return this;
	},

	average: function(){
		var numGrades = this.grades.length;
		var result = 0;
		for( var i = 0; i < numGrades; i++){
			result += grades[i];
		}
	}
}
