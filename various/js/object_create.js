function Shape() { // superclass
  this.x = 0;
  this.y = 0;
}

Shape.prototype.move = function(x,y) {
  this.x += x;
  this.y += y;
  console.info('shape moved by %d x and %d y', x,y)
}

function Rectangle() { // subclass
  Shape.call(this); // calling super constructor
}

Rectangle.prototype.area = function() {
  return this.x * this.y;
}

// subclass     extends       superclass
Rectangle.prototype = Object.create(Shape.prototype);
Rectangle.prototype.constructor = Rectangle;

var rect = new Rectangle();

console.log('rect instance of Rectangle: ',(rect instanceof Rectangle));
console.log('rect instance of Shape: ',(rect instanceof Shape));
rect.move(1,1);

function ThingThatDoesThings() {
  this.a = 'a';
  this.b = 'b';
}

ThingThatDoesThings.prototype.print = function() {
  console.log(this.a,this.b,'te te te','he he he');
};

function Square() {
  Shape.call(this);
  Rectangle.call(this);
  ThingThatDoesThings.call(this);
}

Square.prototype = Object.create(Rectangle.prototype); // inherit
Square.prototype.constructor = Square;

function mixin(dest,src) {
  for (var prop in src) {
    if(src.hasOwnProperty(prop)) {
      dest[prop] = src[prop];
    }
  }
}
mixin(Square.prototype,ThingThatDoesThings.prototype); // mixin

var sq = new Square();

console.log('sq instance of Shape: ',(sq instanceof Shape));
console.log('sq instance of Rectangle: ',(sq instanceof Rectangle));
console.log('sq instance of ThingThatDoesThings: ',(sq instanceof ThingThatDoesThings));
console.log('sq instance of Square: ',(sq instanceof Square));
sq.move(1,1);
sq.print();

// ------------------------------------------------------------------------------------

var o;
o = Object.create(null); // null is prototype

o = {}; // is equivalent to
o = Object.create(Object.prototype);

o = Object.create(Object.prototype, {

  foo : { writable : true,
          configurable : true,
          value : 'hello' },
  bar : { configurable : false,
          get : function() { return 10 ;},
          set : function(value) { console.log('setting `o.bar` to',value); } }
});

function Constructor() {}
o = new Constructor();
// is equivalent to
o = Object.create(Constructor.prototype);
// but if there is actual init code in the Constructor function,
// Object.create() cannot reflect it

// Create a new object whose prototype is a new, empty object
// and    add a single property 'p', with value 42.

o = Object.create({}, { p : {value:42} });

// by default, properties A R E  N O T writable, enumerable, or configurable:
o.p = 24;
o.p; // => 42

o.q = 12;
for (var prop in o) {
  console.log(prop)
}
// => 'q'

delete o.p; // false

// to specify an ES3 property,
o2 = Object.create({}, {
  p : {
    value : 42,
    writable : true,
    enumerable : true,
    configurable : true
  }
});


