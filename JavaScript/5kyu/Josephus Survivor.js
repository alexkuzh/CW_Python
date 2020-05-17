// https://www.codewars.com/kata/555624b601231dc7a400017a/train/javascript
function josephusSurvivor(n, k) {
    //your code here
    let a = [...Array(n + 1).keys()];
    a.shift()
    while (a.length > 1) {
        for (let i = 1; i < k; i++) {
            a.push(a[0])
            a.shift()
        }
        a.shift()
    }
    return a[0]
}

// function josephusSurvivor(n,k){
//     res=1;
//     for (var i=1;i<=n;i++) res=(res+k-1)%i+1;
//     return res;
// }

// function josephusSurvivor(n,k){
//     var people = [],
//         p = 0;
//     for (var i = 0; i < n; i++) { people.push(i+1); }
//     while (people.length > 1) {
//         p = (p + k - 1) % people.length;
//         people.splice(p, 1);
//     }
//     return people.pop();
// }
console.log(josephusSurvivor(7, 3))