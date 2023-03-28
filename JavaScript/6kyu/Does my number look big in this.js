// https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/javascript
/*
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    array
    String
    Number
    split
    map
    for of
 */
function narcissistic(value) {
    // Code me to return true or false
    let b = String(value).split('').map(Number)
    let acc = 0
    for (x of b){
        acc += x**b.length
    }
    return acc == value
}

console.log(narcissistic(371))