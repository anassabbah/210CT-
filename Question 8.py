#remove vowels from a string
def no_vowels(v):
    if not v: #checks for an empty string
        return v
    elif v[0] in "AEIOUaeiou": #checks if first character in string is a vowel
        return no_vowels (v[1:]) #checks the rest of the string
    return v[0] + no_vowels(v[1:]) 
print(no_vowels("Beautiful"))
