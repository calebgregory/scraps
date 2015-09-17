// A function that flattens at all levels
// e.g., [1,[2,[[3,[[4,[[5]]]],6],7],8,9]] => [1,2,3,4,5,6,7,8,9]
function flatten(array) {
  var newArr = [];
  (function recur(arr){
    arr
    .forEach(function(el) {
      if (Array.isArray(el) {
        recur(el);
      } else {
        newArr.push(el);
      }
    });
  })(array);
  return newArr;
}
