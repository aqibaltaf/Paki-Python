def countVowel(sentence):
    vowels = "aeiou"
    count = 0

    for letter in vowels:
        count += sentence.count(letter)

    return count

def isIsogram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        if string.lower().count(letter) > 1:
            return False
    return True

def getMiddle(s):
    length = int(len(s)/2)
    if len(s)%2 == 0: return(s[length-1: length+1]) 

    return(s[length:length+1])

def removeVowel(string_):
    vowels = ["a","e","i","o","u", "A" , "E", "I", "O", "U"]
    
    '''Check if any letter from the array is in the string then remove it'''
    for letter in vowels:
        if letter in string_:
            string_ = string_.replace(letter,"")
            
    return string_
