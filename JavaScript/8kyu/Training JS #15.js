// https://www.codewars.com/kata/57256064856584bc47000611
function howManySmaller(arr,n){
    //coding here..
    let i = 0
    for (x of arr){
        if (x.toFixed(2)< n){
            i++
        }
    }
    return i
}