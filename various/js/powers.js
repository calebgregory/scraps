/*
 * A command line app for generating
 * powers of 2 from 2^0 to 2^32
 */
for (var x = 1, i = 0; i < 32; i++) {
  console.log( "2^%d = %d" , i, x);
  x += x;
}
