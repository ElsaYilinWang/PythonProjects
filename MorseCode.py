#--- Convert text into Morse Code ---#

# Create a dictionary to store Morse Code
MorseCode = {'A': '.-',
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'W': '.--',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--..',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.',
             '0': '-----',
             ', ': '--..--',
             '.': '.-.-.-',
             '?': '..--..',
             '/': '-..-.',
             '-': '-....-',
             '(': '-.--.',
             ')': '-.--.-'
             }

# Ask users for input

def convertToMorseCode():
    ans = ""
    user_input = input("Please enter a sentence: \n")
    user_input = user_input.upper()

    for char in user_input:
        if char in MorseCode:
            ans += MorseCode[char]
        else:
            ans += " "
    print("-"*10)
    print("The Morse Code is: \n")
    print(ans)

convertToMorseCode()
