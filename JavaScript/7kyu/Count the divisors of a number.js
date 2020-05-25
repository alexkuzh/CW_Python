// https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/javascript
function getDivisorsCnt(n){
    let a = new Set()
    if (n == 1) {return 1}
    for (start = 1; start <n; start ++){
        if (n % start == 0)
        {
            a.add(n/start)
            a.add(start)
        }
    }
    return a.size
}


console.log(getDivisorsCnt(30))