// https,//www.codewars.com/kata/5270d0d18625160ada0000e4/train/javascript
function score( dice ) {
    // Fill me in!
    let obj = [['111',1000], ['666',600], ['555', 500], ['444',400], ['333',300], ['222',200], ['1',100], ['5',50]];
    let s = dice.sort().join('');
    let a = 0;
    for (let i = 0; i<5; i++){
        for (let j = 0; j<8; j++){
            if (s.indexOf(obj[j][0]) >=0) {
                a += obj[j][1];
                s = s.replace(obj[j][0],'');
            }
        }
    }
    return a
}

console.log(score([3,4,5,3,3]))