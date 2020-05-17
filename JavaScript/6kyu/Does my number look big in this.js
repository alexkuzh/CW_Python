// https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/javascript
function narcissistic(value) {
    // Code me to return true or false
    let arr= String(value).split('').map(Number)
    let a = 0
    for (x of arr){
        a += x**arr.length
    }
    return a == value
}


console.log(narcissistic(371))