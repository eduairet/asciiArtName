# Modules required for this program
import unidecode, importlib, re, os, alphabetDict
from termcolor import colored
from random import choice
importlib.reload(alphabetDict)
from alphabetDict import lettersDict

# Name generator function that takes a word for parameter:
def asciiNameGenerator(word, randomize=False):
    # Gets the letterform rows from alphabetDict.lettersDict
    rows = len(lettersDict[word[0]].draw)
    # Start the string with the Ascii Art with two line breaks
    asciiName = '\n\n'
    # Drawing loop that goes row by row through every letter of the word
    for row in range(rows):
        for letter in word:
            # Joins every letter row in a string and adds it to our Ascii name 
            if randomize:
                rowString = ''.join(lettersDict[letter].randomizeDraw()[row])
            else:
                rowString = ''.join(lettersDict[letter].draw[row])
            asciiName += f'{rowString}  '
        # Starts a new line
        asciiName += '\n'
    # Adds a final line break and return the string
    asciiName += '\n'
    return asciiName

questionColor = 'green'
# Ask user for a word input
print(colored('\nPlease, write your name\n', questionColor))
word = unidecode.unidecode(input(str)).upper()
# Repeat if the name doesn't match the requirements
while len(re.findall('[^A-Z\s]+', word)) != 0: # It uses RegEx to check the pattern
    print(colored('\nTry again and just use letters and spaces\n', 'red'))
    word = unidecode.unidecode(input(str)).upper()
# Define randomize
print(colored('\nDo you want to randomize the art? (yes/no)\n', questionColor))
myChoice = input(str).lower()
if myChoice in ['yes','y', 'ye', '']:
   randomize = True
elif myChoice in ['no','n']:
   randomize = False
else:
   randomize = False
# Call the function and save the art in a variable
currentAsciiWord = asciiNameGenerator(word, randomize)
# Add the art to an txt file for the blog in the docs directory
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(f'{projectPath}/docs/htmlOutput.txt', 'a', encoding='utf-8') as htmlOutput:
    htmlOutput.write('<p class="code">\n')
    htmlOutput.write(currentAsciiWord.replace('\n', '<br/>\n'))
    htmlOutput.write('</p>')

# Print the art in the console with a random color
colors = ['cyan', 'yellow', 'blue']
print(colored(currentAsciiWord, choice(colors)))