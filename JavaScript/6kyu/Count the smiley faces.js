// https://www.codewars.com/kata/583203e6eb35d7980400002a/train/javascript
//return the total number of smiling faces in the array
function countSmileys(arr) {
    a = 0
    for (x of arr){
        // console.log(x.match(/^[:;][-~]{0,1}[D)]$/gm))
        if (x.match(/^[:;][-~]{0,1}[D)]$/gm)) { a++}
    }
    return a
}

console.log(countSmileys([ ':---)', '))', ';~~D', ';D' ]))