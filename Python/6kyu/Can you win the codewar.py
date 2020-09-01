# https://www.codewars.com/kata/5e3f043faf934e0024a941d7/train/python
def codewar_result (codewarrior, opponent) :
    vic = 0
    codewarrior.sort()
    opponent.sort()
    for x in range(len(codewarrior)):
        print(vic)
        print(codewarrior,opponent)
        s_cod = sorted(set(codewarrior))
        s_opp = sorted(set(opponent))
        if s_cod[-1] < s_opp[-1]:
            codewarrior.remove(s_cod[0])
            opponent.remove(s_opp[-1])
            print(s_cod[0],'-',s_opp[-1])
            vic -=1
        elif s_cod[-1] > s_opp[-1]:
            codewarrior.remove(s_cod[-1])
            opponent.remove(s_opp[-1])
            print(s_cod[0],'-',s_opp[-1])
            vic +=1
        elif s_cod[-1] == s_opp[-1]:
            if len(s_cod)>1 and len(s_opp)>1:
                f_opp = list(filter(lambda x: x < s_cod[-1], s_opp))
                f_cod = list(filter(lambda x: x > f_opp[-1], s_cod))
                if f_cod:
                    print(f_cod[0],'-',f_opp[-1])
                    codewarrior.remove(f_cod[0])
                    opponent.remove(f_opp[-1])
                    vic += 1
            else:
                codewarrior.remove(s_cod[-1])
                opponent.remove(s_opp[-1])
                print(s_cod[-1],'-',s_opp[-1])

    print(vic)

    return 'Victory' if vic > 0 else 'Defeat' if vic < 0 else 'Stalemate'

# print(codewar_result([2, 4, 3, 1], [4, 5, 1, 2])) #victory
# print(codewar_result([1, 4, 1], [1, 5, 3])) #Stalemate
# print(codewar_result([1, 2, 2, 1], [3, 1, 2, 3])) #defeat
# print(codewar_result([1, 1, 1, 1], [1, 1, 1, 1]))
print(codewar_result([5], [6]))
# print(codewar_result([2, 1, 3, 1, 1, 3, 3, 2, 3, 1, 1, 1, 3, 1, 3, 1, 3, 3, 1, 2, 3, 3, 1, 3], [4, 4, 1, 4, 3, 1, 4, 4, 3, 2, 1, 2, 1, 3, 3, 1, 4, 4, 3, 2, 3, 2, 4, 1]))
# print(codewar_result([2, 4, 4, 2, 5, 2, 2] ,[4, 4, 2, 5, 2, 2, 3]))