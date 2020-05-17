// https://www.codewars.com/kata/586f6741c66d18c22800010a/train/javascript
const sequenceSum = (begin, end, step) => {
    // May the Force be with you
    let a = 0
    for (i =begin; i <=end; i+=step){
        a +=i
    }
    return a
};