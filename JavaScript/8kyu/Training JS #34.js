// https://www.codewars.com/kata/5733f948d780e27df6000e33
function cutCube(volume,n){
    //coding here...
    return Math.round(Math.pow(n,1/3))**3 == n && Math.round(Math.pow(volume/n,1/3))**3 == volume/n
}
