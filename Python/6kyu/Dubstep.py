# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
def song_decoder(song):
    return ' '.join(list(filter(lambda a: a != '', song.split('WUB'))))

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))