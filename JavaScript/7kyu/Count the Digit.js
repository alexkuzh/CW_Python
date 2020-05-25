// https://www.codewars.com/kata/566fc12495810954b1000030/train/javascript
function nbDig(n, d) {
    // your code
    let s = ''
    for (let x = 0; x<=n; x ++){
        s +=(x**2).toString()
    }
    return s.split(d).length-1
}

console.log(nbDig(10,1))
