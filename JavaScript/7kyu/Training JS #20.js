// https://www.codewars.com/kata/57284d23e81185ae6200162a
function topSecret(str){
    let o = '';
    for (x of str) o = o + String.fromCharCode((x.charCodeAt() >= 97 && x.charCodeAt() <= 99 || x.charCodeAt() >= 65 && x.charCodeAt() <= 67) ? x.charCodeAt() + 23 : (x.charCodeAt() <= 64) ? x.charCodeAt() : x.charCodeAt() - 3)
    return o;
}
//question1: The top secret file number is...
answer1="3054";
//question2: Super agent's name is...
answer2="LBjj";
//question3: He stole the treasure is...
answer3="Marie's husband";