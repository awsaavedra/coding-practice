/*
	aka, a line FIFO- first in first out

	methods: dequeue (remove) , enqueue (add), peek
*/

function Queue() {
	this.dataStore = [];
	this.enqueue = enqueue;
	this.dequeue = dequeue;
	this.front = front;
	this.back = back;
	this.toString = toString;
	this.isEmpty = isEmpty;
}

function enqueue(element){
	this.dataStore.push(element);
}

function dequeue(element){
	return this.dataStore.shift();
}

function front(){
	return this.dataStore[0];
}

function back(){
	return this.dataStore[this.dataStore.length-1];
}

function isEmpty(){
	if(this.dataStore.length <= 0){
		return true;
	}else{
		return false;
	}
}

function toString(){
	var retStr = "";
	for( var i = 0; i < this.dataStore.length; i++){
		retStr += this.dataStore[i] + "\n";
	}
	return retStr;
}

/////////////////////////////////////testin programs\\\\\\\\\\\\\\\\\\\\\\\\\\
var q = new Queue();
q.enqueue("Meredith");
q.enqueue("Cynthia");
q.enqueue("Jennifer");
console.log(q.toString());
console.log("deque: " + q.dequeue("Jennifer"));
console.log("Front of queue: " + q.front());
console.log("Back of queue: " + q.back());
