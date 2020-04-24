import  re
def is_valid_IP(strng):

    return len(re.findall(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",strng)) == 1
    #print(x)
    #return re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",strng)

print(is_valid_IP('012.255.56.1'))