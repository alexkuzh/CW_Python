# file_def = 'quest.txt'
# print("Hello Guest! Type you name here")
# NAME = input()
# with open(file_def, 'w') as name:
#     name.write(NAME.title())
# with open(file_def, 'r') as quest: # И нет возможности, кроме json выдать инфу?
#     print(quest.readline())

alien_3 = {'color': 'green', 'points': 5, 'x_position': 1}
x = 2
alien_3['x_position'] = alien_3['x_position'] + x  # А другие оперторы , почему не срабатывают
print("New x-position: " + str(alien_3['x_position']))
# НЕ ЯСНО КАК МЕНЯТЬ ЗНАЧЕНИЯ, ведь не в коде ж....
del alien_3['color']
print(alien_3)
alien4 = {'color': 'gray', 'points': 8, 'x_position': 0, 'y_position': 50, 'speed': 'fast'}
# print(alien4)
if alien4['speed'] == 'slow':  # The slow movement is 1
    x_increment = 1
elif alien4['speed'] == 'medium':  # The medium movement is 2
    x_increment = 2
else:
    x_increment = 3  # The fast movement is 3
alien4['y_position'] = alien4['y_position'] + x_increment
print(alien4['y_position'], str(alien4['y_position']))
# Здесь спросить , как менять другие значения при перемещении, кроме х, и почему два значения.
# и почему в команде принт в учебнике + , вместо значений через запятую