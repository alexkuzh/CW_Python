// https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript
function isPangram(string){
    //...
    let s = 'abcdefghijklmnopqrstuvwxyz'
    let a = string.match(/\w+/g).join('').toLowerCase()
    for (x of s){
        if (a.search(x)==-1) {return false}
    }
    return true
}


console.log(isPangram('Is "Pack my box with five dozen liquor jugs." a pangram ?'))