// https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/javascript
class SequenceSum{
    static showSequence(count) {
        if (count < 0) { return  count + '<0'}
        if (count == 0) { return '0=0'}
        // let s = ''
        let s  = []
        let a = 0
        // for (let i=0; i<count; i++){
        for (let i=0; i<=count; i++){
            // s += i.toString()+'+'
            s.push(i)
            a += i
        }
        // a += count
        // s+= count.toString() +' = '+a.toString()
        let d = s.join('+') +' = '+a.toString()
        return d //s
    }
}

a = new SequenceSum()
console.log(SequenceSum.showSequence(6))