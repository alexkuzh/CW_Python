// https://www.codewars.com/kata/5be8e1bb88c754481f000466/javascript
function moonRaiting(num){
    s = ''
    for (i = 0; i < 10 ; i++)
        s += 'o'
    // console.log(Math.floor(n/2))
    if (n%2) {
        s += 'c'
        i+=1
    }
    for (k = i; k<5; k++)
        s += 'x'
    return s
}


moonRating=r=>{s ='';for(i=0;i<5;i++){r>=1.5?s +='o':r>=0.5?s+='c':s+='x';r-=2}return s}

console.log(moonRaiting(7))