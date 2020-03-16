// https://www.codewars.com/kata/572cb264362806af46000793
function threeInOne(arr){
    //coding here...
    let arr_o = []
    const arrSum = arr => arr.reduce((a,b) => a + b, 0)
    for (let i = 0; i < arr.length / 3; i++){
        arr_o = arr_o.concat(arrSum(arr.slice(i*3,i*3+3)))
    }
    return arr_o
}
