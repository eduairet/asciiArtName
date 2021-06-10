from random import choice
# Define your letters list from a string
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
letters = letters.replace('', '\r')
lettersList = [letter for letter in letters.split('\r') if letter != '']
# Create a character class to hold the character and its methods
class Character:
    def __init__(self, name):
        self.name = name
        self.draw = []
    def drawCharacter(self):
        for i, row in enumerate(self.draw):
            for j, character in enumerate(row):
                if character:
                    self.draw[i][j] = self.name
                else:
                    self.draw[i][j] = ' '
    def randomizeDraw(self):
        randomDraw = self.draw
        for i, row in enumerate(randomDraw):
            for j, character in enumerate(row):
                if character != ' ':
                    randomDraw[i][j] = choice(lettersList[:-2])
        return randomDraw
# Create a dict with every letter
lettersDict = {}
# Fill the letters dictionary
for letter in lettersList:
    lettersDict[letter] = Character(letter) # This empty list will be populated later with the letters
# Variables for drawing, names are in order to get better contrast
W, _ = True, False
# Here all the letters are drawn
lettersDict[' '].draw = [
    [_,_,_,_],
    [_,_,_,_],
    [_,_,_,_],
    [_,_,_,_],
    [_,_,_,_],
    [_,_,_,_],
    [_,_,_,_]
]
lettersDict['A'].draw = [
    [_,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W]
]
lettersDict['B'].draw = [
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,_]
]
lettersDict['C'].draw = [
    [_,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,_,_],
    [W,W,_,_,_,_],
    [W,W,_,_,_,_],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_]
]
lettersDict['D'].draw = [
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,_]
]
lettersDict['E'].draw = [
    [W,W,W,W,W],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,_],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,W]
]
lettersDict['F'].draw = [
    [W,W,W,W,W],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,_,_,_],
    [W,W,W,W,_],
    [W,W,_,_,_],
    [W,W,_,_,_]
]
lettersDict['G'].draw = [
    [_,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,_,_],
    [W,W,_,W,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_]
]
lettersDict['H'].draw = [
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W]
]
lettersDict['I'].draw = [
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W],
    [W,W]
]
lettersDict['J'].draw = [
    [_,_,_,W,W],
    [_,_,_,W,W],
    [_,_,_,W,W],
    [_,_,_,W,W],
    [W,W,_,W,W],
    [W,W,_,W,W],
    [_,W,W,W,_]
]
lettersDict['K'].draw = [
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,W,W,_],
    [W,W,W,W,_,_],
    [W,W,_,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W]
]
lettersDict['L'].draw = [
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,_,_],
    [W,W,W,W]
]
lettersDict['M'].draw = [
    [W,W,_,_,_,_,W,W],
    [W,W,W,_,_,W,W,W],
    [W,W,W,_,_,W,W,W],
    [W,W,W,W,W,W,W,W],
    [W,W,_,W,W,_,W,W],
    [W,W,_,W,W,_,W,W],
    [W,W,_,_,_,_,W,W]
]
lettersDict['N'].draw = [
    [W,W,_,_,_,W],
    [W,W,W,_,_,W],
    [W,W,W,W,_,W],
    [W,_,W,W,_,W],
    [W,_,W,W,W,W],
    [W,_,_,W,W,W],
    [W,_,_,_,W,W]
]
lettersDict['O'].draw = [
    [_,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_]
]
lettersDict['P'].draw = [
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,_],
    [W,W,_,_,_,_],
    [W,W,_,_,_,_]
]
lettersDict['Q'].draw = [
    [_,W,W,W,W,_,_],
    [W,W,_,_,W,W,_],
    [W,W,_,_,W,W,_],
    [W,W,_,_,W,W,_],
    [W,W,_,_,W,W,_],
    [W,W,_,_,W,W,_],
    [_,W,W,W,W,W,W]
]
lettersDict['R'].draw = [
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,W,W,W,_],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W]
]
lettersDict['S'].draw = [
    [_,W,W,W,_],
    [W,W,_,_,W],
    [W,W,W,_,_],
    [_,W,W,W,_],
    [_,_,W,W,W],
    [W,_,_,W,W],
    [_,W,W,W,_]
]
lettersDict['T'].draw = [
    [W,W,W,W,W,W],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_]
]
lettersDict['U'].draw = [
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_]
]
lettersDict['V'].draw = [
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_],
    [_,_,W,W,_,_]
]
lettersDict['W'].draw = [
    [W,W,_,W,W,_,W,W],
    [W,W,_,W,W,_,W,W],
    [W,W,_,W,W,_,W,W],
    [W,W,_,W,W,_,W,W],
    [W,W,_,W,W,_,W,W],
    [_,W,W,W,W,W,W,_],
    [_,_,W,_,_,W,_,_]
]
lettersDict['X'].draw = [
    [W,W,_,_,_,W],
    [W,W,_,_,_,W],
    [W,W,W,_,W,_],
    [_,_,W,W,_,_],
    [_,W,_,W,W,W],
    [W,_,_,_,W,W],
    [W,_,_,_,W,W]
]
lettersDict['Y'].draw = [
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [W,W,_,_,W,W],
    [_,W,W,W,W,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_],
    [_,_,W,W,_,_]
]
lettersDict['Z'].draw = [
    [W,W,W,W,W,W],
    [_,_,_,_,W,W],
    [_,_,_,W,W,W],
    [_,W,W,W,W,_],
    [W,W,W,_,_,_],
    [W,W,_,_,_,_],
    [W,W,W,W,W,W]
]
# Replace True values with the letter of the character
for letter in lettersDict.values():
    letter.drawCharacter()