var memoize = function(f) {
  var cache = {};

  return function() {
    var arg_str = JSON.stringify(arguments);
    console.log('arg_str:',arg_str)
    cache[arg_str] = cache[arg_str] || f.apply(f, arguments);
    console.log('arguments:',arguments);
    return cache[arg_str];
  };
};

module.exports = memoize;
