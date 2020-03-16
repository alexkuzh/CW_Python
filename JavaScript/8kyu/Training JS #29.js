// https://www.codewars.com/kata/5731861d05d14d6f50000626
function bigToSmall(arr){
    let a=[].concat(...arr);
    return a.sort(function(a, b) {return a - b;}).reverse().join('>')
}
