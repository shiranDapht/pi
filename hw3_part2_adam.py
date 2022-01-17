'''
def get_palindrom_dict(string : str):
    pals = {}
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            s = string[i:j]
            if(s and s == s[::-1]):
                pals[len(s)] = pals[len(s)] + [s] if(len(s) in pals) else [s]
    return pals


def check_match(string : str):
    if(len(string)%2 != 0):
        return False
    if(not string):
        return True
    s1 = string[1::2]
    s2 = string[0::2]
    tranformation = {k:v for k,v in zip(s1,s2)}
    transformed_s1 = ''.join([tranformation[c] for c in s1])
    return s2 == transformed_s1
'''
# just cause I can :P
def get_palindrom_dict(string : str):
    return {sub[0]:[subsub[1][0] for subsub in [[len(string[i:j]),[string[i:j]]] for i in range(len(string)) for j in range(i+1, len(string)+1) if string[i:j] and string[i:j] == string[i:j][::-1]] if len(subsub[1][0]) == sub[0]] for sub in [[len(string[i:j]),[string[i:j]]] for i in range(len(string)) for j in range(i+1, len(string)+1) if string[i:j] and string[i:j] == string[i:j][::-1]]}

def check_match(string : str):
    return len(string)%2 == 0 and string[0::2] == ''.join([{k:v for k,v in zip(string[1::2],string[0::2])}[c] for c in string[1::2]])
