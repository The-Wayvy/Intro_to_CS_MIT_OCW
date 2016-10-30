def two_right(phrase):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    translation = ''
    for character in phrase:
        if character == " " or character == "." or character == "'" or character == "(" or character == ")":
            translation = translation + character
        else:
            new_index = alphabet.index(character) + 2
            if new_index < 26:
                translation = translation + alphabet[new_index]
            else: translation = translation + alphabet[new_index - 26]
    return translation


print two_right("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")


                
