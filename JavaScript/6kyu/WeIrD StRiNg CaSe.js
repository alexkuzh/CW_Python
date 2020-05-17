// https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/javascript
function f(t) {
    let r = ''
    for (let i = 0; i < t.length; i++) {
        r+= i % 2 === 0?t[i].toUpperCase():t[i].toLowerCase()
        }
    return r
}


function toWeirdCase(string){
    a = string.split(' ')
    let d = []
    for (x of a) {
        d.push(f(x))
    }
    return d.join(' ')
}


console.log(toWeirdCase('This is a test'))
let d = 'ddd'
console.log(f(d))