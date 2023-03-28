// https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/javascript
function validatePIN (pin) {
    let p = pin.search(/(^\d{6}$)|(^\d{4}$)/gi)
    console.log(p)
    if (p>=0) {
        return true
    }
    return false
}

const pin = ("12345")
console.log(validatePIN (pin))