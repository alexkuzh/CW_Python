// https://www.codewars.com/kata/57274562c8dcebe77e001012
function cutIt(arr){
    //coding here...
    let l = 1000
    let a = []
    for (x of arr){if (x.length < l) l = x.length}
    for (x of arr){
        a.push(x.slice(0,l))
    }
    return a
}