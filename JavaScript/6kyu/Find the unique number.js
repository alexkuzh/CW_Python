// https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/javascript
function findUniq(arr) {
    // do magic
    let s = [...new Set(arr)]
    for (x of s){
        c = 0
        for (let n =0; n< arr.length; n++){
            if (arr[n] == x){
                c++
                if (c>1){ return s[1]}
            }
            if (n>2 && c==1){return x}
        }
    }
}

console.log(findUniq([10,0,10,10,10]))