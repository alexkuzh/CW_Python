//https://www.codewars.com/kata/572fdeb4380bb703fc00002c
function isolateIt(arr){
    a = []
    for (x of arr){
        if (x.length%2 == 0){
            a.push(x.slice(0,x.length/2) + '|' +x.slice(x.length/2))
        }
        else {
            a.push(x.slice(0,x.length/2) + '|' +x.slice(x.length/2+1))
        }
    }
    return a
}
