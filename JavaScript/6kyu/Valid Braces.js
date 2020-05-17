// https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/javascript
function validBraces(braces){
    let a = braces.length+1
    while (braces.length!=a){
        a = braces.length
        if (braces.indexOf('()')>=0) {braces = braces.replace('()','')}
        if (braces.indexOf('{}')>=0) {braces = braces.replace('{}','')}
        if (braces.indexOf('[]')>=0) {braces = braces.replace('[]','')}
    }
    return braces.length == 0
}

console.log(validBraces('[]'))