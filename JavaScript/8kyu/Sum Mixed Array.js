// https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/javascript
function sumMix(x){
    return Number(x.reduce((a,b) => Number(a) + Number(b)))
}

console.log(sumMix([9, 3, '7', '3']))