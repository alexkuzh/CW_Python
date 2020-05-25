//  https://www.codewars.com/kata/52f3149496de55aded000410/train/javascript
function sumDigits(number) {
    let a = 0
    while (number>9){
        a +=number%10
        number  = Math.floor(number/10)
    }
    return a+number
}

console.log(sumDigits(123))