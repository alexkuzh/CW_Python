// https://www.codewars.com/kata/5663f5305102699bad000056/train/javascript
function mxdiflg(a1, a2) {
    if (a1.length ==0 || a2.length==0) { return -1}
    a1.sort(function(a, b){return a.length-b.length})
    a2.sort(function(a, b){return a.length-b.length})
    let a1_min = a1[0].length
    let a2_min = a2[0].length
    let a1_max = a1[a1.length-1].length
    let a2_max = a2[a2.length-1].length

    if (a1.length == 1 && a2.length == 1) {return Math.abs(a1_min-a2_min)}
    return Math.max(Math.abs(a1_min - a2_max), Math.abs(a1_max - a2_min))
}

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

console.log(mxdiflg(a1,a2))