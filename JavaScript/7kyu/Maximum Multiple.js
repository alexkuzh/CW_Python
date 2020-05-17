// https://www.codewars.com/kata/5aba780a6a176b029800041c/train/javascript
function maxMultiple(divisor, bound){
    //your code here
    for (x=bound; x>0; x--){
        if (x%divisor==0){return x}
    }
}