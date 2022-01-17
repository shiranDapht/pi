def isPalindrome(str):
    return str == str[::-1]

def get_palindrom_dict(str):
    new_dict = {}
    for i in str:
        new_list = []
        for j in str:
            word = str[j : j + i]
            if(isPalindrome(word)):
                new_list.append(word)
    
    new_dict.update(i, new_list)
    return new_dict



def check_match(str):
    if(len(str)%2):
        return False
    even, odd = str[::2], str[1::2]
    even_dict = get_palindrom_dict(even)
    odd_dict = get_palindrom_dict(odd)
    word_len = len(even)
    if(word_len in even_dict and word_len in odd_dict):
        return True
    elif():
        return False


