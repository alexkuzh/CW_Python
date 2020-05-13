// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/javascript
var countSheep = function (num){
    //your code here
    a = ''
    for (let i=1; i<=num; i++){
        a += i + ' sheep...'
    }
    return a
}

console.log(countSheep(3))