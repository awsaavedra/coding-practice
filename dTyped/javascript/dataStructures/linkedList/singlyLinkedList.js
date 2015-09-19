/*
	The primary thing to know about linked lists is that they are 
	great for inserting anywhere, as opposed to arrays which are good for insertion
	at the end of the array (think push method)

	pros:
		-fast insertion anywhere in list
		-linkedlists are not fixed in size and not awkward to grow since they
			are not required to be contiguous in memory (no random access) 
	cons:
		-not contiguous in memory so traversal is necessary when searching O(n),
		aka no random access

	NOTE: when random access is required, use an array.	

	Linked list structure(singly linked):

	[head node ] --> [ data1 | pntr1] --> [ data2 | pntr2] -->...[ data_n | pntr_n] --> null
		
		linkedlist methods:
			add, remove, etc.
*/

//constructor function for creating nodes
function Node(element){
	this.element = element; //element, for storing nodes data
	this.next = null;  
}

//provides functionality for LL (linkedList) 
//methods: find, insert, remove, display (show)
function LList() {
	this.head = new Node("head");
	this.find = find;
	this.insert = insert;
	this.findPrevious = findPrevious;
	this.remove = remove;
	this.display = display;
}

//find(), helper function for finding specific data
function find(item){
	var currNode = this.head; //setting current node to head
	while( currNode.element != item){
		currNode = currNode.next; //traversing through LL
	} //NOTE: if no data is found, currNode will be return as null
	return currNode; //returns the node storing the data being looked for
}

//insert (add) function to add nodes to LL
function insert(newElement, item){
	var newNode = new Node(newElement); //new node object
	var current = this.find(item); //calls helper function
	newNode.next = current.next; //referencing in order, (???)
	current.next = newNode;
}

//shows all nodes w/ data in them (not head node)
function display() {
	var currNode = this.head;
	while (!(currNode.next == null)) {
		console.log(currNode.next.element);
		currNode = currNode.next;
	}
}

function findPrevious(item) {
	var currNode = this.head;
	while (!(currNode.next == null) && (currNode.next.element != item)) {
		currNode = currNode.next;
	}
	return currNode;
} 

//removing nodes in a LL 
function remove(item) {
	var prevNode = this.findPrevious(item);
	if (!(prevNode.next == null)) {
		prevNode.next = prevNode.next.next;
	}
}


/////////////////////////////////////Testing LL\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
var cities = new LList();
cities.insert("Conway", "head");
cities.insert("Russellville", "Conway");
cities.insert("Carlisle", "Russellville");
cities.insert("Alma", "Carlisle");
cities.display();
console.log();
cities.remove("Carlisle");
cities.display();
