// https://www.codewars.com/kata/5722b3f0bd5583cf44001000
function giveMeFive(obj){
    //coding here
    let arr = [];
    for (i in obj){
        if (i.length == 5 ) arr.push(i);
        if (obj[i].length == 5 ) arr.push(obj[i]);
    }
    return arr;
}
