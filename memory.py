# memory game for platics in waterways / oceans
import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
from time import sleep

bgcolour = ('lightgreen') #Sets bgcolour as global variable


def init():
        #Declaring constrants
        gridSize = 15
        buttonRow = 0
        gameRow = 0
        gameCol = 0
        cards = []

        #Creating tkinter window 
        root = Tk()
        root.title('Memory')
        root.geometry('1920x1080')
        root.config(bg=bgcolour)

        #Empty list will add the file list whihc is shuffled here.
        card_names = []
        #open file and read the content in a list
        with open(r'carddeck.txt', 'r') as fp: #Opens the carddeck.txt file in read only (MUST BE CREATED THRU main.py FIRST)
            for line in fp:
                x = line[:-1]
                # add current item to the list
                card_names.append(x)
        card_names = card_names*2 #Doubles the card_names list so that we have two of each card.
        #Since we have appended to the list by doubling will shuffl the card_names list again
        random.shuffle(card_names)

        cardsFrame = tk.Frame(root)
        cardsFrame.grid(rows=1, column=2)
        for card in range(len(card_names)):
            cardImg = (Image.open(f"cards/{card_names[card]}.gif"))
            cardImg = cardImg.resize((108 ,151)) # Halfs the size of the large playing cards. For the loading screen this is cause we don't need it to be large
            cardImg = ImageTk.PhotoImage(cardImg)
            cards.append(cardImg)
            card += 1
            button=tk.Button(cardsFrame, image=cardImg, command=lambda card = card:  get_card(card))
            if buttonRow < gridSize:
                button.grid(row=gameRow,column=gameCol)
                buttonRow += 1
                gameCol += 1
            if buttonRow == gridSize:
                gameRow += 1        
                buttonRow = 0
                gameCol = 0
        
        root.mainloop()
    
def get_card(card):
    print (card)


#Initalizes the application, when loaded
init()
