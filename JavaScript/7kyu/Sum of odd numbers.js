/*https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/javascript
* Sum of odd numbers */
function rowSumOddNumbers(n) {
//1 3 7 13 21 => 1 1+1*2  1+2*3 1+2*2*3 1+2*3*4 1+2*6
    return n * n * n
}
console.log(rowSumOddNumbers(42))