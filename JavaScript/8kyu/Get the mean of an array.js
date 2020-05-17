// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/javascript
function getAverage(marks){

    return  Math.floor(marks.reduce((a, b) => a + b, 0) / marks.length)
}

console.log(getAverage([1,2,3,3,5,]))