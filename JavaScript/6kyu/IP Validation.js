// https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/javascript
function isValidIP(str) {
    return str.search(/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/) === 0
}

console.log(isValidIP('137.255.156.100'))