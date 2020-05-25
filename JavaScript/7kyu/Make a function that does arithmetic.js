//https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/javascript
function arithmetic(a, b, operator){
    //your code here!
    let arr = {"add":"+", "subtract":"-", "divide":"/", "multiply":"*"}
    return eval(a.toString()+arr[operator]+b.toString())
}

console.log(arithmetic(1, 2, "add"))