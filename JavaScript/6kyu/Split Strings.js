// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/javascript
function solution(str){
    if (str.length%2==1) {str += '_'}
    a = []
    for (let i = 0; i <str.length; i+=2){
        a.push(str[i]+str[i+1])
    }
    return a
}

console.log(solution('abcdef'))