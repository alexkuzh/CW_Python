// https://www.codewars.com/kata/5732d3c9791aafb0e4001236
function roundIt(n){
    //coding here...
    let s = n.toString().split('.')
    if (s[0].length < s[1].length) return Math.ceil(n)
    if (s[0].length > s[1].length) return Math.floor(n)
    return Math.round(n)
}
