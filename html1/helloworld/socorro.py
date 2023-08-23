vowels = ["a", "e", "i", "o", "u"]

def stringIncludesMoreVowelsThanConsonants(s, v = 0, c = 0):
    if len(s) == 1:
        if s[0].lower() in vowels:
            return (v + 1) > c
        return v > (c + 1)

    if s[0].lower() in vowels:
        return stringIncludesMoreVowelsThanConsonants(s[1:], v + 1, c)
    return stringIncludesMoreVowelsThanConsonants(s[1:], v, c + 1)
    
print(stringIncludesMoreVowelsThanConsonants("HakunaMatata"))