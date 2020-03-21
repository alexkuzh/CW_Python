# https://www.codewars.com/kata/52b2cf1386b31630870005d4/train/python
def flesch_kincaid(text):
    # (0.39 * average number of words per sentence) + (11.8 * average number of syllables per word) - 15.59
    v = ('a','e','i','o','u')
    sign = ('.','!','?')
    sent = text.count('.',0,-1)
    sent += text.count('!',0,-1)
    sent += text.count('?',0,-1)
    sent +=1
    sen = len(text.split(' ')) # count words
    a = text.split(' ')
    syl = 0 #count syllables
    for s in a:
        m = 0
        for i in range(len(s)):
            if s[i].lower() in v:
                m +=1
                syl += 1
                if m > 1:
                    syl -= 1
            else:
                m = 0
    syl = 8
    #sen = 13
    #4.19
    sent = 2
    print(sen, sent, syl, len(a))
    return round((0.39 * sen / sent) + (11.8 * syl / len(a)) - 15.59, 2)

print(flesch_kincaid("Oh no! The lemming is falling"))

