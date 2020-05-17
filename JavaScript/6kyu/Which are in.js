// https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/javascript
function inArray(array1,array2){
    a = []
    for (x of a1){
        let flag = true
        for (y of a2){
            if (x && y && y.search(x)>=0) {
                if (flag) {
                    a.push(x)
                    flag = false
                }
            }
        }
    }
    return a.sort()
}
let a1 = [ 'ou', 'oint' ]
let a2 =
    [ 'a',
        'apidock',
        '(since',
        'your',
        'am',
        'you',
        'have',
        'would',
        'versioning;',
        'perfect',
        'known',
        'glad',
        'the',
        'In',
        'I',
        '1.9?',
        'not' ]

console.log(inArray(a1,a2))