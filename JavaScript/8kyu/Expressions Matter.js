// https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
function expressionMatter(a, b, c) {
    if (a==1 && c==1) {return b + 2
    }else if (a==1){return (1 + b) * c
    }else if (c==1){return a  * (b + 1)
    }else if (b==1){
        if (a>c){return a * (1  + c)}
        else {return (a + 1) * c}
    }else {return a * b * c}
}
