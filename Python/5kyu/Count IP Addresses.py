# https://www.codewars.com/kata/526989a41034285187000de4/train/python
def get_num(st):
    s_a = st.split('.')
    s_a.reverse()
    s_n = 0
    for i in range(len(s_a)):
        s_n += int(s_a[i])*(256**i)
    return s_n


def ips_between(start, end):
    # TODO
    return get_num(end) - get_num(start)


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.1.0"))
print(ips_between("20.0.0.10", "20.0.1.0"))