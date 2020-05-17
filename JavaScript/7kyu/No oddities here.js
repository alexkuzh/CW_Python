//https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/javascript
function noOdds( values ){
    // Return all non-odd values
    a = []
    for (x of values)
        if (x%2 == 0) {a.push(x)}
    return a
}

console.log(noOdds([0,1,2,3]))