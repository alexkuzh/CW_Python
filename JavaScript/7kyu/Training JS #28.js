// https://www.codewars.com/kata/57308546bd9f0987c2000d07
function mirrorImage(arr){
    //coding here...
    const reversedNum = num => num.toString().split('').reverse().join('')
    for (i=0;i<arr.length-1; i++){
        if (arr[i] == reversedNum(arr[i+1])) return [arr[i],arr[i+1]]
    }
    return [-1,-1]
}
