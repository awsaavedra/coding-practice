function pairwise(arr, arg) {
  var result = 0,
      newArr = [],
      indices = [];

  for(var k = 0; k < arr.length; k++) {
    newArr.push(arr[k]);
  }

  for(var i = 0; i < arr.length; i++) {
    for(var j = 0; j < newArr.length; j++) {

      if(i !== j) {

        if(arr[i] + newArr[j] === arg && indices.indexOf(i) === -1 && indices.indexOf(j) === -1) {
          result += i + j;
          indices.push(i, j);
        }
      }
    }
  }

  return result;
}
