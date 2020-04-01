/*https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/javascript
Array plus array */
function arrayPlusArray(arr1, arr2) {
    return arr1.concat(arr2).reduce((a,b) => a+b,0);
}
console.log(arrayPlusArray([1,2,3],[4,5,6]))