
function multiplyAll(arr) {
  var product = 1;
  // Only change code below this line
  for(var i = 0; i < arr.length; i++){
    for(var k = 0; k < arr[i].length; k++){
      product *= arr[i][k];
    }
  }
  // Only change code above this line
  return product;
}

// Modify values below to test your code
console.log(multiplyAll([[1,2],[3,4],[5,6,7]]));
