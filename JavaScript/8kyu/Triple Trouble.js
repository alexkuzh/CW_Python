// https://www.codewars.com/kata/5704aea738428f4d30000914/train/javascript
function tripleTrouble(one, two, three){
    //Solution
    s = ''
    for (let i = 0; i<one.length; i++){
        s += one[i]+two[i]+three[i]
    }
    return s
}

console.log(tripleTrouble("this","test","lock"))