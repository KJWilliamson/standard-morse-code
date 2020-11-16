#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code: Standard Edition
"""
__author__ = 'Kamela Williamson'
# working with Mai and Drew

from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    MORSE_2_ASCII
    # your code here
    # strip takes out trailing. spaces in front and back
    morse = morse.strip()
    # splitting by 3 spaces. each word we split is by 3 spaces
    words_list = morse.split("   ")
    w_translate = []
    for word in words_list:
        letter_list = word.split(" ")
        l_translate = []
        for letter in letter_list:
            translate = MORSE_2_ASCII[letter]
            l_translate.append(translate)
        w_translate.append("".join(l_translate))
    result = " ".join(w_translate)

    return result


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")

    print("\nCompleted.")
