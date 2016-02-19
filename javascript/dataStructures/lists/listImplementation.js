function List(){ //initialized list function
	this.listSize = 0;
	this.pos = 0;
	this.dataStore = []; //init empty array to store elements
	this.clear = clear;
	this.find = find;
	this.toString = toString;
	this.insert = insert;
	this.append = append;
	this.remove = remove;
	this.front = front;
	this.end = end;
	this.prev = prev;
	this.next = next;
	this.length = length;
	this.currPos = currPos;
	this.moveTo = moveTo;
	this.getElement = getElement;
	this.length = length;
	this.contains = contains;
}

//append adds an element in the next available location (end)
//the list is incremented by 1 using this.listSize++
function append(list){
	this.dataStore[this.listSize++] = element;
}

//find, the helper function for remove
function find(element){
	for( var i = 0; i < this.dataStore.length; i++){
		if(this.dataStore[i] == element){
			return i;
		}
	}
	return -1; //-1 is returned if the element is not found
}

function length(){
	return this.listSize;
}

//view elements of a list
function toString(){
	return this.dataStore; //technically returns an array obj,
												 // but just more practical
}

function remove(element) {
	var foundAt = this.find(element);
	if (foundAt > -1) {
		this.dataStore.splice(foundAt,1);
		--this.listSize;
		return true;
	}
	return false;
}

function insert(element, after){
	var insertPos = this.find(after);
	if(insertPos > -1){
		this.dataStore.splice(insertPos + 1,0, element);
		++this.listSize;
		return true;
	}
	return false;
}

function clear(){
	delete this.dataStore; //nukes data store
	this.dataStore = []; //recreates empty array
	this.listSize = this.pos = 0; //returns list size to original state, 0
}

function contains(element){
	for(var i = 0; i < this.dataStore.length; i++){
		if(this.dataStore[i] == element){
			return true;
		}
	}
	return false; 
}

//list traversal
function front() {
	this.pos = 0;
}

function end() {
	this.pos = this.listSize-1;
}

function prev() {
	if (this.pos > 0) {
		--this.pos;
	}
}

function next() {
	if (this.pos < this.listSize-1) {
		++this.pos;
	}
}

function currPos() {
	return this.pos;
}

function moveTo(position) {
	this.pos = position;
}

function getElement() {
	return this.dataStore[this.pos];
}

for(names.front(); names.currPos() < names.length(); names.next()) {
	print(names.getElement());
}
