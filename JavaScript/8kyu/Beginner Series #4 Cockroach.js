/*https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/javascript
Beginner Series #4 Cockroach */
function cockroachSpeed(s) {
    //km/h => cm/sec
    return Math.floor(s * 1000 / 36)
}
console.log(cockroachSpeed(1.08))