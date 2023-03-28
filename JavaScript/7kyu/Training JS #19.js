// https://www.codewars.com/kata/5728203b7fc662a4c4000ef3
function alienLanguage(str){
    let a = ''
    let s = str.toUpperCase().split(' ');
    for (x of s){
        a = a +x.slice(0,x.length-1) + x[x.length -1].toLowerCase() + ' '
    }
    return a.trim()
}

console.log(alienLanguage('asdsad asdasd'))