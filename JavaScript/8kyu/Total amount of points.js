// https://www.codewars.com/kata/5bb904724c47249b10000131/train/javascript
function count(s) {
    if (s[0] > s[2]){return 3}
    if (s[0] == s[2]){return 1}
    if (s[0] < s[2]){return 0}
}

function points(games) {
    // your code here
    const reducer = (accumulator, currentValue) => accumulator + count(currentValue)
    return games.reduce(reducer)
}

function p(games){
    a = 0
    for (x of games){
        a += count(x)
    }
    return a
}

// console.log(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
console.log(p(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))