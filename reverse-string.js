/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
    var reversed = '';
    var i;

    for (i = s.length - 1; i >= 0; i--) {
        reversed += s[i];
    }

    return reversed;
};

var main = function() {
  console.log(reverseString('hello'));
}

if (require.main === module) {
  main();
}
