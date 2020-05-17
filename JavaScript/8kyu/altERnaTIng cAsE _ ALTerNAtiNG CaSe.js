// https://www.codewars.com/kata/56efc695740d30f963000557/train/javascript
String.prototype.toAlternatingCase = function () {
    // Define your method here :)
    var output = "";

    for (var i = 0; i < this.length; i++) {

        var ch = this[i];

        if (ch === ch.toUpperCase()) {
            output += ch.toLowerCase();
        } else {
            output += ch.toUpperCase();
        }
    }

    return output;
}