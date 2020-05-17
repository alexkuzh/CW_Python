// https://www.codewars.com/kata/534ffb35edb1241eda0015fe/train/javascript
function scoreHand(cards) {
    a = 0
    count_ace = 0
    for (x of cards){
        if (x == "J" || x == "Q" || x == "K") {a+=10}
        else if (x== "A"){ count_ace++; a+=11}
        else {a+=parseInt(x)}
        if (a>21 && count_ace>0){a-=10; count_ace--}
    }
    if (a>21 && count_ace>0){a-=10; count_ace--}
    return a
}


console.log(scoreHand(['A', 'J', 'A']))