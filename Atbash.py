def encrypt(txt):
    txt = txt.upper()
    N = ord('Z') + ord('A')
    ans = ''
    return ans.join([chr(N - ord(x)) for x in txt])