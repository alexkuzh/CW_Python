// https://www.codewars.com/kata/5601409514fc93442500010b/train/javascript
function betterThanAverage(classPoints, yourPoints) {
    // Your code here
    return classPoints.reduce((a, b) => a + b) / classPoints.length <= yourPoints
}

console.log(betterThanAverage([2, 3], 5))