// https://www.codewars.com/kata/5722fd3ab7162a3a4500031f
function whatNumberIsIt(n){
    //coding here
    if (Number.isNaN(Number(n)) )return 'Input number is Number.NaN';
    switch (n){
        case Number.NEGATIVE_INFINITY:
            return 'Input number is Number.NEGATIVE_INFINITY';
        case Number.POSITIVE_INFINITY:
            return 'Input number is Number.POSITIVE_INFINITY';
        case Number.MAX_VALUE:
            return 'Input number is Number.MAX_VALUE';
        case Number.MIN_VALUE:
            return 'Input number is Number.MIN_VALUE';
        default: return 'Input number is '+n
    }
}