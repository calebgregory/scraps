function c (arr) {

  var objs = arr.map(function(el,i,a) {
    var obj = '{ "' + i + '" : "' + el + '" }';
    return obj;
  })

  var json = '{';
  json+= objs.reduce(function(prev,curr,i,a) {
    return i < (a.length-1) ?
      prev.concat(curr + ',') :
      prev.concat(curr);
  },'');
  json+= '}';

  return json;
}

function d (arr) {

  var objs = arr.map(function(el,i,a) {
    var obj = '{  \n  "word" : "' + el + '",';
    obj+= '\n  "dist" : "' + Math.random().toPrecision(7) + '"';
    obj+= '\n  }'
    return obj;
  })

  var json = '{\n';
  json+= objs.reduce(function(prev,curr,i,a) {
    return i < (a.length-1) ?
      prev.concat(curr + ',') :
      prev.concat(curr);
  },'');
  json+= '\n}';

  return json;

}
