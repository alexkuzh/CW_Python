// https://www.codewars.com/kata/539de388a540db7fec000642/train/javascript
function checkCoupon(enteredCode, correctCode, currentDate, expirationDate){
    return enteredCode == correctCode && Date.parse(currentDate)<=Date.parse(expirationDate)
}

var msec = Date.parse("March 21, 2012");
console.log(msec)