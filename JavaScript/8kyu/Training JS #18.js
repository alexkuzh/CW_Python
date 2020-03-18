// https://www.codewars.com/kata/57280481e8118511f7000ffa
function splitAndMerge(string, separator) {
    let s = string.split(' ')
    let a = []
    for (x of s){a.push(x.split('').join(separator))}
    return a.join(' ')
}
