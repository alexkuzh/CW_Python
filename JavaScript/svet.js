// function findDeletedNumber(arr, mixArr) {
//     if (arr.length == 0 && mixArr.length==0) {
//         return 0}
//     mixArr.sort((a, b) => a - b)
//     for (i = 0; i < arr.length; i++) {
//         if (arr[i] != mixArr[i]) {
//             return arr[i]}
//         else if (arr[i] == mixArr[i] && arr.length == mixArr.length) {
//             return 0}
//     }
// }
//
// // console.log(findDeletedNumber([],[]))
function test(arr) {
    if (Array.isArray(arr)){
        let s = "Array is defined"
        if (arr.length>0){

            return s + " and not empty"
        }
        else {
            return s + " and empty"
        }
    }
    else {
        return "It is not an array or not defined"
    }
}
//
if (Array.isArray(arr) && arr.length) {
    console.log(1) // array exists and is not empty
}

console.log(test([]))
console.log(test([1,2]))
console.log(test(10))
console.log(test('qwerty'))

// //
// let arr = []
// console.log(arr == [])  //false
// console.log(arr == null) //false
