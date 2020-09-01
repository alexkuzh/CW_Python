# https://www.codewars.com/kata/598980a41e55117d93000015/train/python
def decode(m):
    translation = { '|)' :'d','_\\~':'s','|-|':'h','|^':'p','|_|':'u','|_':'l','[-':'e','|\/|':'m',
                '()':'o','__':' ', ']3':'b','t':'~|~','|':'i','~|~':'t','`/':'y','/?':'r','/\\':'a','|\\|':'n',
                '/<':'k', '(':'c', '/=':'f', '_T':'j','><':'x','(_,':'g','()_':'q','\/\/':'w','~/_':'z','\/':'v'
                    }
    a = m.split(m[0])
    s = ''
    for m in a:
        if m in translation:
            s += m.replace(m,translation[m])
    return(s[::-1])

print(decode("++|\|+|\|+++|^+++|-|+++/?+++\/\/+(+++()+`/+|^+|)+++\/++|\/|++]3++]3+++|-|+++|^+++|\/|+++|^+++()++|+++()_++(_,+++/?+\/\/++_\~++|+/\+++/\+|+++/=+|\/|+++_\~++~|~++|^++><++`/+++]3+++|)+\/\/+()_+++|)+++()_+++|\|++[-+/<+~|~++|+++(_,+++]3++\/+_\~+++/=+|_++`/+++`/+|_|++_\~++|+++|_+|+(+()+++/?+_\~+><+/<+|^++_T+++\/\/++|-|+(_,+|\|+++"))



# 'bdtxnjgtgahicwujfaq rykkutgidxaoa  igtrguvoc zdxxllcahjhbvxf ekslpnxkgnfxfktfjvsaxbarbpavfgbndrpxlxwluefxaherdvxzzlbocfhtggvhcujarnskccqxbwssoctrdxvydpkgydyzhtj'
# 'bdtxnjgtgahicwujfaqmrykkutgidxaoammigtrguvocmzdxxllcahjhbvxfmekslpnxkgnfxfktfjvsaxbarbpavfgbndrpxlxwluefxaherdvxzzlbocfhtggvhcujarnskccqxbwssoctrdxvydpkgydyzhtj'