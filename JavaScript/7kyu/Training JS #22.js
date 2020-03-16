// https://www.codewars.com/kata/572ab0cfa3af384df7000ff8
function shuffleIt(arr,...a){
    //coding here...
    for (x of a) [arr[x[0]],arr[x[1]]] = [arr[x[1]],arr[x[0]]];
    return arr
}