# Define your letters list from a string
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = letters.replace('', ' ')
lettersList = letters.split()
# Create a dict with every letter
lettersDict = {}
# Fill the letters dictionary
for letter in lettersList:
    lettersDict[letter] = [] # This empty list will be populated later with the letters
# Variables for drawing, names are in order to get better contrast
W, _ = True, False
# Here all the letters are drawn
lettersDict['A'] = [
    [_,W,W,W,_],
    [W,_,_,W,W],
    [W,_,_,W,W],
    [W,_,_,W,W],
    [W,W,W,W,W],
    [W,_,_,W,W],
    [W,_,_,W,W]
]
lettersDict['B'] = [
    [W,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,W,_]
]
lettersDict['C'] = [
    [_,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,_,_,W],
    [_,W,W,W,_]
]
lettersDict['D'] = [
    [W,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,W,_]
]
lettersDict['E'] = [
    [W,W,W,W,W],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,_],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,W]
]
lettersDict['F'] = [
    [W,W,W,W,W],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,_],
    [W,W,_,_,_],
    [W,W,_,_,_]
]
lettersDict['G'] = [
    [_,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,_],
    [W,W,_,W,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [_,W,W,W,_]
]
lettersDict['H'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,W,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W]
]
lettersDict['I'] = [
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W]
]
lettersDict['J'] = [
    [_,_,W,W],
    [_,_,W,W],
    [_,_,W,W],
    [_,_,W,W],
    [W,_,W,W],
    [W,_,W,W],
    [_,W,W,_]
]
lettersDict['K'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,W,_],
    [W,W,W,_,_],
    [W,W,_,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W]
]
lettersDict['L'] = [
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,W,W]
]
lettersDict['M'] = [
    [W,W,_,_,_,W,W],
    [W,W,_,_,W,W,W],
    [W,W,W,_,W,W,W],
    [W,_,W,W,_,W,W],
    [W,_,W,W,_,W,W],
    [W,_,_,_,_,W,W],
    [W,_,_,_,_,W,W]
]
lettersDict['N'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,_,W],
    [W,W,W,_,W],
    [W,_,W,W,W],
    [W,_,_,W,W],
    [W,_,_,W,W]
]
lettersDict['O'] = [
    [_,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [_,W,W,W,_]
]
lettersDict['P'] = [
    [W,W,W,W,_],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,W,W,_],
    [W,W,_,_,_],
    [W,W,_,_,_]
]
lettersDict['Q'] = [
    [_,W,W,W,_,_],
    [W,W,_,_,W,_],
    [W,W,_,_,W,_],
    [W,W,_,_,W,_],
    [W,W,_,_,W,_],
    [W,W,_,_,W,_],
    [_,W,W,W,W,W]
]
lettersDict['S'] = [
    [_,W,W,W,_],
    [W,W,_,_,W],
    [W,W,W,_,_],
    [_,W,W,W,_],
    [_,_,W,W,W],
    [W,_,_,W,W],
    [_,W,W,W,_]
]
lettersDict['T'] = [
    [W,W,W,W,W,W],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_]
]
lettersDict['U'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [_,W,W,W,_]
]
lettersDict['V'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,_,W],
    [_,W,W,W,_],
    [_,_,W,_,_]
]
lettersDict['W'] = [
    [W,W,_,W,W,_,W],
    [W,W,_,W,W,_,W],
    [W,W,_,W,W,_,W],
    [W,W,_,W,W,_,W],
    [W,W,_,W,W,_,W],
    [_,W,W,W,W,W,W],
    [_,_,W,_,_,W,_]
]
lettersDict['X'] = [
    [W,W,_,_,W],
    [W,W,_,_,W],
    [W,W,_,W,_],
    [_,W,W,W,_],
    [_,W,W,W,W],
    [W,_,_,W,W],
    [W,_,_,W,W]
]
lettersDict['Y'] = [
    [W,W,_,_,_,W],
    [W,W,_,_,_,W],
    [W,W,_,_,_,W],
    [_,W,W,_,W,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_]
]
lettersDict['Z'] = [
    [W,W,W,W,W],
    [_,_,_,W,W],
    [_,_,_,W,W],
    [_,_,W,W,_],
    [_,W,W,_,_],
    [W,W,_,_,_],
    [W,W,W,W,W]
]
# Replace True values with the letter of the character
for key, value in lettersDict.items():
    for i, row in enumerate(value):
        for j, character in enumerate(row):
            if character:
                lettersDict[key][i][j] = key
            else:
                lettersDict[key][i][j] = ' '

