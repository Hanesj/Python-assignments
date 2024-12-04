import string
def solution(s):
    string_list = []
    decoded = ""
    alphabet_lowercase = list(string.ascii_lowercase)
    index = None
    
    """Loops through characters in string, if lowercase letter reverse alphabet add corresponding letter at index
       Otherwise do nothing."""
    for char in s:
        
        if str.islower(char):
            if char not in alphabet_lowercase:
                string_list.append(char)
            else:
                index = alphabet_lowercase.index(char)
                alphabet_lowercase.reverse()
                string_list.append(alphabet_lowercase[index])
        
        else:
            string_list.append(char)

    for char in string_list:
        decoded += char
    
    return decoded
