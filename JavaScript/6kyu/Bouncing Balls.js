// https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/javascript
function bouncingBall(h,  bounce,  window) {
    // your code here
    i = -1
    if (bounce > 0 && bounce < 1) {
        while (h > window) {
            i+=2
            h *= bounce
        }
    }
    return i
}

console.log(bouncingBall(3.0, 0.66, 1.5))

// function bouncingBall(h,  bounce,  window) {
//     var rebounds = -1;
//     if (bounce > 0 && bounce < 1) while (h > window) rebounds+=2, h *= bounce;
//     return rebounds;
// }