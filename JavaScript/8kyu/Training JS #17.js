// https://www.codewars.com/kata/57277a31e5e51450a4000010
function firstToLast(str,c){
    return str.indexOf(c) == -1 ? -1 : str.lastIndexOf(c) - str.indexOf(c)
}
