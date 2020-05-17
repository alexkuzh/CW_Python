// https://www.codewars.com/kata/57f36495c0bb25ecf50000e7/train/javascript
function findSum(n) {
    a = 0
    for (i=3; i<=n; i++){
        if (i%3 == 0 || i%5 == 0){ a+=i}
    }
    return a
}