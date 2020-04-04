//https://www.codewars.com/kata/57cff961eca260b71900008f/train/javascript
const sym = [97,101,105,111,117];

function f(value,index,a) {
    a[index] = sym.indexOf(value)>-1 ? String.fromCharCode(value) : value;
}

function isVow(a){
    a.map(f)
    return a
}

console.log(isVow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))