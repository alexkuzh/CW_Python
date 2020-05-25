// https://www.codewars.com/kata/52829c5fe08baf7edc00122b/train/javascript
Array.prototype.numberOfOccurrences = function(n) {
    return this.filter(x => x === n).length;
}