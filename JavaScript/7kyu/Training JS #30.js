// https://www.codewars.com/kata/573156709a231dcec9000ee8
function tailAndHead(arr){
    let m = []
    for (let i =0; i<arr.length-1; i++){
        m = m.concat(parseInt(arr[i].toString()[arr[i].toString().length-1])+ parseInt(arr[i+1].toString()[0]))
    }
    return m.reduce((a,b) => a*b)
}
