// https://www.codewars.com/kata/57238ceaef9008adc7000603
function colorOf(r,g,b){
    return '#'+('00'+r.toString(16)).slice(-2)+('00'+g.toString(16)).slice(-2)+('00'+b.toString(16)).slice(-2);
}