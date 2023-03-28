function high(words) {
    const alpha = ' abcdefghijklmnopqrstuvwxyz';
    const score = word => word.split('').reduce((a, b) => a + alpha.indexOf(b), 0);
    console.log(score(words))
    return words
        .split(' ')
        .map((word, pos) => ({ word: word, pos: pos, score: score(word) }))
        .sort((a, b) => a.score - b.score || b.pos - a.pos)
        .pop()
        .word;
}


console.log(high('man i need a taxi up to ubud'))