# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
def generate_hashtag(s):
#your code here
    if len(s) ==0 or len(s) > 140 : return False
    return '#'+s.title().replace(' ','')

print(generate_hashtag(' Hello there thanks for trying my Kata'))