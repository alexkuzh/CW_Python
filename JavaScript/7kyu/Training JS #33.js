// https://www.codewars.com/kata/5733d6c2d780e20173000baa
function maxMin(arr1,arr2){
    let sum = []
    for (let i=0; i<arr1.length; i++){
        sum.push(Math.abs(arr1[i] - arr2[i]));
    }
    sum.sort((a,b)=>a-b)
    return [sum[sum.length-1],sum[0]]
}