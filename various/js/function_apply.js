function minOfArray(arr) {
  var min = Infinity;
  var QUANTUM = 32768;

  for(var i = 0, len = arr.length;
      i < len;
      i+= QUANTUM) {

    var submin = Math.min.apply( null,
      arr.slice(i, Math.min(i + QUANTUM, len)));

    min = Math.min(submin, min);

  }

  return min;
}

var min = minOfArray([5,6,2,3,7]);

// --- 'MONKEY-PATCHING', THEY SAY

var originalfoo = someobject.foo;
someobject.foo = function() {
  // Do stuff before calling function
  console.log(arguments);
  // Call the function as it would have been called normally
  originalfoo.apply(this,arguments);
  // Run stuff after, here
}
