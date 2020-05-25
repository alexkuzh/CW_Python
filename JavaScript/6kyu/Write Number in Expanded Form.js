// https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/javascript
function expandedForm(num) {
    // Your code here
    let s = String(num)
    let a = ''
    for (let i = 0; i < s.length; i++){
        if (s[i] != '0') {
            a += s[i].padEnd(s.length-i,'0') + ' + '
        }
    }
    return a.substring(0,a.length-3)
}

console.log(expandedForm(70304))