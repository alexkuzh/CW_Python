// https://www.codewars.com/kata/57216d4bcdd71175d6000560
function padIt(str,n){
    i = 0
    while (i<n){
        (i % 2 == 0)? str = '*' + str : str = str + '*'
        i ++
    }
    return str
}
