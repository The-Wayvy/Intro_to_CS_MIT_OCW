def compressor(phrase):
    word_list = phrase.split()
    compressed_phrase = ''
    for word in word_list:
        compressed_phrase = compressed_phrase + word
    return compressed_phrase

"""
Is there a built-in compressor function?
"""

print compressor("I love cake")

def Palindromer(phrase):
    our_letters = compressor(phrase)
    if len(our_letters) % 2 == 0:
        first_half = our_letters[:len(our_letters) / 2]
        second_half = our_letters[len(our_letters) - 1:len(our_letters) / 2 - 1:-1]
        if first_half == second_half:
            return True
        else: return False
    else:
        first_half = our_letters[:len(our_letters) / 2]
        second_half = our_letters[len(our_letters) - 1:len(our_letters) / 2:-1]
        if first_half == second_half:
            return True
        else: return False

print Palindromer('kitty')
print Palindromer('coin')
print Palindromer('eatae')
print Palindromer('abba')
        
