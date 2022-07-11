import string

morseCharacters = {
    "a":  ".-",
    "b":  "-...",
    "c":  "-.-.",
    "d":  "-..",
    "e":  ".",
    "f":  "..-.",
    "g":  "--.",
    "h":  "....",
    "i":  "..",
    "j":  ".---",
    "k":  "-.-",
    "l":  ".-..",
    "m":  "--",
    "n":  "-.",
    "o":  "---",
    "p":  ".--.",
    "q":  "--.-",
    "r":  ".-.",
    "s":  "...",
    "a":  "-",
    "u":  "..-",
    "v":  "...-",
    "w":  ".--",
    "x":  "-..-",
    "y":  "-.--",
    "z":  "--..",
    "å":  ".--.-",
    "ä":  ".-.-",
    "ö":  "---.",
    "0":  "-----",
    "1":  ".----",
    "2":  "..---",
    "3":  "...--",
    "4":  "....-",
    "5":  ".....",
    "6":  "-....",
    "7":  "--...",
    "8":  "---..",
    "9":  "----.",
    ".":  ".-.-.-",
    ",":  "--..--",
    "?":  "..--..",
    "!":  "-.-.--",
    " ":  "      "
}

def String2Morse( message: str ):

    # Start with an empty string
    message_code = ""
    
    # Loop through each character in the message you want to convert
    for c in message:
        # Verify that the character is represented in our dictionary, use 'x' if missing
        if c in morseCharacters:
            message_code += morseCharacters[c] + " "
        else:
            message_code += "x "

    # Remove the last trailing space
    if len(message_code) > 1:
        message_code = message_code[:-1]

    return message_code

print( String2Morse( "morse code"))
