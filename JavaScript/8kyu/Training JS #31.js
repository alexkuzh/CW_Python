// https://www.codewars.com/kata/5732b0351eb838d03300101d
function blackAndWhite(arr){
    //coding here...
    if (!Array.isArray(arr)) return "It's a fake array"
    if (arr.indexOf(5)>=0 && arr.indexOf(13)>=0) return "It's a black array"
    return "It's a white array"
}