// https://www.codewars.com/kata/572df796914b5ba27c000c90
function sortIt(arr) {
    let a_new = arr.slice().sort()
    let a_buf = []
    let n = 0
    let kol = 1
    for (let i = 0; i <= a_new.length; i++) {
        if (n != a_new[i]) {
            a_buf.push([kol, n])
            n = a_new[i]
            kol = 1
        } else {
            kol++
        }
    }
    a_buf.shift()
    a_buf.sort(function(a,b){
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
        if (a[1] > b[1]) return -1;
        if (a[1] < b[1]) return 1;
        return 0;
    })
    a_new = []
    for (let i of a_buf){
        n = 0
        while (n<i[0]){
            a_new.push(i[1])
            n++
        }
    }
    return a_new
}