import random
from tkinter import *
from turtle import bgcolor

from PIL import image, ImageTk

bgcolor = ('limegreen') #Sets bgcolour as global variable

root = Tk()

def init():

    root.title('Card Games')
    root.geometry('500x400')
    root.config(bgcolor)


    main_file = open("bridge1.txt", "r")
    file = main_file.readline()
    file = file[:-1]
    cardNums = main_file.readline()
    cardChar = main_file.readlines()
    deck = open(file, "r")
    n = 2
    card_deck = deck.readline()
    cardDeck = ([card_deck[i:i+n] for i in range(0, len(card_deck), n)])
    random.shuffle((cardDeck))



if __name__ == "__main__":
    init()