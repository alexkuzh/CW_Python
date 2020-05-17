// https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/javascript
function inAscOrder(arr) {
    for (i = 0; i < arr.length-1; i ++){
        if (arr[i]>arr[i+1]) {return false}
    }
    return true
}

console.log(inAscOrder([1,6,10,18,22,24,220]))