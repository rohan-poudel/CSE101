def translateWord(word):
    word = word.lower()
    vow = "aeiou"
    cons = "bcdfghjklmnpqrstvwxyz"
    if word[0] in cons and word[1] in vow:
        word = word[1:] + word[0] + 'ay'
    elif word[0] in cons and word[1] in cons:
        word = word[2:] + word[0:2] + 'ay'
    elif word[0] in vow:
        word = word + 'way'
    print(word,end=" ")

# translateWord("or")

def translateSentence(sen):
    sen = sen.lower()
    sen = sen.split()
    for i in range(len(sen)):
        translateWord(sen[i])
    
translateSentence("To be or not to be that is the question.")









