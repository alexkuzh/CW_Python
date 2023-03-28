//https://www.codewars.com/kata/587731fda577b3d1b0001196/train/javascript
String.prototype.camelCase=function(){
    //your code here
    if (this == '') return ''
    let s = this.split(' ')
    let a = []
    for (x of s){
        a.push(x.charAt(0).toUpperCase() + x.slice(1))
        console.log(a)
    }
    return a.join('')
}

console.log('camel case method'.camelCase())