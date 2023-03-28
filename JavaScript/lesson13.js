a = ['qqqqqqq','ssss','aa','eeewwer','fgffgfgfgfggfg']

//вариант с циклом
m = Infinity
s = ''
for (x of a){
    if (x.length<m) {
        m = x.length
        s = x
    }
}
console.log(s)

//вариант с сортировкой по длине
a.sort((a,b)  => a.length -b.length )
console.log(a[0])