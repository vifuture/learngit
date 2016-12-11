def semordnilap(str1,str2):
    if len(str1)!=len(str2):
        return False
    if len(str1) == 1:
        return str1 == str2
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False
    
