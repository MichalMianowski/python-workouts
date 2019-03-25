# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:10:22 2019

@author: MM
"""

# Hangman game

import random
import string
alphabet = string.ascii_lowercase
    

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letters = list(secretWord)
    for let in lettersGuessed:
        while let in letters:
            letters.remove(let)
    if len(letters) == 0:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for let in secretWord:
        if let in lettersGuessed:
            ans += let
        else:
            ans += '_ '
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    listOfLetters = list(alphabet)
    for let in lettersGuessed:
        listOfLetters.remove(let)
    return ''.join(listOfLetters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
 
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    chances = 8
    lettersGuessed = []
    while not isWordGuessed(secretWord, lettersGuessed) and chances >0:
        print("-------------")
        print("You have", chances, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        newLetterInput = input("Please guess a letter: ")
        newLetter = newLetterInput.lower()
        if newLetter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
        elif newLetter in secretWord:
            lettersGuessed.append(newLetter)
            print("Good guess:", getGuessedWord(secretWord,lettersGuessed))
        elif newLetter in alphabet:
            lettersGuessed.append(newLetter)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
            chances -= 1
        else:
            print("That's not a letter, don't cheat!", getGuessedWord(secretWord,lettersGuessed))
    
    if chances == 0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secretWord, ".")
    else:
        print("-------------")
        print("Congratulations, you won!")
    



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

