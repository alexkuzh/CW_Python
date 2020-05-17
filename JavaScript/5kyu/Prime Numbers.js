//https://www.codewars.com/kata/52dd72494367608ac1000416/train/javascript
function isPrime(number) {
    if (number <=1) {
        return false
    }
    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            return false
        }
    }
    return true
}

function getPrimes(start, finish) {
    let a = []
    let fin = finish;
    let st = start
    if (start > finish) {st = finish;fin = start}
    for (let i = st; i <= fin; i++) {
        if (isPrime(i)) {
            a.push(i)
        }
    }
    return a
}

console.log(isPrime(4))
console.log(getPrimes(30, 1).join())