# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order,max_e):
    # code here
    a = []
    for i in order:
        if a.count(i)>=max_e: continue
        a.append(i)
    return a
    #[1,1,3,3,7,2,2,2,2] 3
    #[1, 1, 3, 3, 7, 2, 2, 2]

print(delete_nth([1,1,3,3,7,2,2,2,2],3))