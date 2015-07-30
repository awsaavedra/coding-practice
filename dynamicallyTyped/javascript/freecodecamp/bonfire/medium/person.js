var Person = function(firstAndLast) {
  this.firstAndLast = firstAndLast;  
  var arr = this.firstAndLast.split(" ");
  this.first = arr[0];
  this.last = arr[1];
  this.blank = 0;
  this.blank1 = 0;
  this.blank2 = 0;
};

Person.prototype.getFirstName = function(){
	return this.first;
};
Person.prototype.getLastName = function(){
	return this.last;
};
Person.prototype.getFullName = function(){
	return this.firstAndLast;
};

Person.prototype.setFirstName = function(first){
	this.first = first;
};
Person.prototype.setLastName = function(last){
	this.last = last;
};
Person.prototype.setFullName = function(firstAndLast){
	this.firstAndLast = firstAndLast;
};


var bob = new Person('Bob Ross');
bob.getFullName();
