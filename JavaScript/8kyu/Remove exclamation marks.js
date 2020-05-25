// https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/javascript
function removeExclamationMarks(s) {
    while (s.search('!')>=0){
        s = s.replace('!','')
    }
    return s
}

console.log(removeExclamationMarks('ssdsd!!!!sdfsdf'))