// https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/javascript
function f(t) {
    let a = 0
    for (x of t){
        a += x.charCodeAt(0)-96
    }
    return a
}

function high(x){
    a = x.split(' ')
    m = 0
    w = []
    for (n of a){
        if (m<f(n)){m=f(n); w=n}
    }
    return w
}

console.log(high('what time are we climbing up the volcano'))

console.log('a'.charCodeAt(0))