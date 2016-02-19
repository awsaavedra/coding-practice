/*
	refresher on BST:	
		insert- O(log(n))
		deletion - log (n)
		basically all log(n) unless you get an insertion case of ALL larger numbers
		in ascending order,e.g. 50, 60, 70, 80, 90. Then O(n)
		
				example of BST:
							56
						/		 \
					22			81
				/		\		/		\
			 10	  30	77	92

1. Set the root node to be the current node.

2. If the data value in the inserted node is less than the data value in the current node,
set the new current node to be the left child of the current node. If the data value
in the inserted node is greater than the data value in the current node, skip to step
4.

3. If the value of the left child of the current node is null , insert the new node here
and exit the loop. Otherwise, skip to the next iteration of the loop.

4. Set the current node to be the right child of the current node.

5. If the value of the right child of the current node is null , insert the new node here
and exit the loop. Otherwise, skip to the next iteration of the loop.
*/

function Node(data, left, right){
	this.data = data;
	this.left = left;
	this.right = right;
	this.show = show; //showing data
}

function show(){
	return this.data;
}

function BST(){
	this.root = null;
	this.insert = insert;
	this.inOrder= inOrder;
}

//all actual logic in insertion
function insert(data) {
var n = new Node(data, null, null);
if (this.root == null) {
this.root = n;
}
else {
var current = this.root;
var parent;
while (true) {
parent = current;
if (data < current.data) {
current = current.left;
if (current == null) {
parent.left = n;
break;
}
}
else {
current = current.right;
if (current == null) {
parent.right = n;
break;
}
}
}
}
}

function inOrder(node) {
if (!(node == null)) {
inOrder(node.left);
console.log(node.show() + " ");
inOrder(node.right);
}
}

var nums = new BST();
nums.insert(23);
nums.insert(45);
nums.insert(16);
nums.insert(37);
nums.insert(3);
console.log("Inorder traversal: ");
inOrder(nums.root);
