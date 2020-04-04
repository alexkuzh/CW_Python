// https://www.codewars.com/kata/595aa94353e43a8746000120/train/javascript
const arrSum = arr => arr.reduce((a,b) => a + b, 0)
function findDeletedNumber(arr, mixArr) {
    // your code
    return arr.reduce((a,b) => a + b, 0) - mixArr.reduce((a,b) => a + b, 0)
}