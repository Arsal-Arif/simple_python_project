def translator(phrase):

    translation = ""

    for letter in phrase:
        if letter in "Aa":
            if letter.islower():
                translation = translation + "1"
            else:
                translation = translation + "1"
        elif letter in "Bb":
            if letter.islower():
                translation = translation + "!"
            else:
                translation = translation + "!"
        elif letter in "Cc":
            if letter.islower():
                translation = translation + "2"
            else:
                translation = translation + "2"
        elif letter in "Dd":
            if letter.islower():
                translation = translation + "@"
            else:
                translation = translation + "@"
        elif letter in "Ee":
            if letter.islower():
                translation = translation + "3"
            else:
                translation = translation + "3"
        elif letter in "Ff":
            if letter.islower():
                translation = translation + "#"
            else:
                translation = translation + "#"
        elif letter in "Gg":
            if letter.islower():
                translation = translation + "4"
            else:
                translation = translation + "4"
        elif letter in "Hh":
            if letter.islower():
                translation = translation + "$"
            else:
                translation = translation + "$"
        elif letter in "Ii":
            if letter.islower():
                translation = translation + "5"
            else:
                translation = translation + "5"
        elif letter in "Jj":
            if letter.islower():
                translation = translation + "%"
            else:
                translation = translation + "%"
        elif letter in "Kk":
            if letter.islower():
                translation = translation + "6"
            else:
                translation = translation + "6"
        elif letter in "Ll":
            if letter.islower():
                translation = translation + "^"
            else:
                translation = translation + "^"
        elif letter in "Mm":
            if letter.islower():
                translation = translation + "7"
            else:
                translation = translation + "7"
        elif letter in "Nn":
            if letter.islower():
                translation = translation + "&"
            else:
                translation = translation + "&"
        elif letter in "Oo":
            if letter.islower():
                translation = translation + "8"
            else:
                translation = translation + "8"
        elif letter in "Pp":
            if letter.islower():
                translation = translation + "*"
            else:
                translation = translation + "*"
        elif letter in "Qq":
            if letter.islower():
                translation = translation + "9"
            else:
                translation = translation + "9"
        elif letter in "Rr":
            if letter.islower():
                translation = translation + "("
            else:
                translation = translation + "("
        elif letter in "Ss":
            if letter.islower():
                translation = translation + ")"
            else:
                translation = translation + ")"
        elif letter in "Tt":
            if letter.islower():
                translation = translation + "10"
            else:
                translation = translation + "10"
        elif letter in "Uu":
            if letter.islower():
                translation = translation + ")!"
            else:
                translation = translation + ")!"
        elif letter in "Vv":
            if letter.islower():
                translation = translation + "12"
            else:
                translation = translation + "12"
        elif letter in "Ww":
            if letter.islower():
                translation = translation + "!@"
            else:
                translation = translation + "!@"
        elif letter in "Xx":
            if letter.islower():
                translation = translation + "14"
            else:
                translation = translation + "14"
        elif letter in "Yy":
            if letter.islower():
                translation = translation + "!$"
            else:
                translation = translation + "!$"
        elif letter in "Zz":
            if letter.islower():
                translation = translation + "16"
            else:
                translation = translation + "16"
        
    print(translation)


translator(input("Enter a phrase: "))


def morse_code_translator(phrase):
    translation = ""

    for letter in phrase:
        if letter in "Aa":
            translation = translation + ".-~"
        elif letter in "Bb":
            translation = translation + "-...~"
        elif letter in "Cc":
            translation = translation + "-.-.~"
        elif letter in "Dd":
            translation = translation + "-..~"
        elif letter in "Ee":
            translation = translation + ".~"
        elif letter in "Ff":
            translation = translation + "..-.~"
        elif letter in "Gg":
            translation = translation + "--.~"
        elif letter in "Hh":
            translation = translation + "....~"
        elif letter in "Ii":
            translation = translation + "..~"
        elif letter in "Jj":
            translation = translation + ".---~"
        elif letter in "Kk":
            translation = translation + "-.-~"
        elif letter in "Ll":
            translation = translation + ".-..~"
        elif letter in "Mm":
            translation = translation + "--~"
        elif letter in "Nn":
            translation = translation + "-.~"
        elif letter in "Oo":
            translation = translation + "---~"
        elif letter in "Pp":
            translation = translation + ".--.~"
        elif letter in "Qq":
            translation = translation + "--.-~"
        elif letter in "Rr":
            translation = translation + ".-.~"
        elif letter in "Ss":
            translation = translation + "...~"
        elif letter in "Tt":
            translation = translation + "-~"
        elif letter in "Uu":
            translation = translation + "..-~"
        elif letter in "Vv":
            translation = translation + "...-~"
        elif letter in "Ww":
            translation = translation + ".--~"
        elif letter in "Xx":
            translation = translation + "-..-~"
        elif letter in "Yy":
            translation = translation + "-.--~"
        elif letter in "Zz":
            translation = translation + "--..~"
        elif letter in "1":
            translation = translation + ".----~"
        elif letter in "2":
            translation = translation + "..---~"
        elif letter in "3":
            translation = translation + "...--~"
        elif letter in "4":
            translation = translation + "....-~"
        elif letter in "5":
            translation = translation + ".....~"
        elif letter in "6":
            translation = translation + "-....~"
        elif letter in "7":
            translation = translation + "--...~"
        elif letter in "8":
            translation = translation + "---..~"
        elif letter in "9":
            translation = translation + "----.~"
        elif letter in "0":
            translation = translation + "-----~"
        elif letter in " ":
            translation = translation + "?"
        final_translation = translation + "~"
        # return final_translation

    print(final_translation)
    

morse_code_translator(input("Enter a phrase: "))