import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

from PIL import Image, ImageTk

bgcolour = ('limegreen') #Sets bgcolour as global variable


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


class load():
    def __init__(self):
        try:
            global cardDeck
            #Creating tkinter window
            self.root = tk.Tk()
            self.root.title('Card Games')
            self.root.geometry('500x250')
            self.root.config(bg=bgcolour)
            self.loadingLabel = tk.Label(self.root, text="Loading...", bg=bgcolour, font=('verdana', 40), fg='green') #f user is on a slow pc the loading label should say loading, So the user knows something is happening.
            self.loadingLabel.place(x=100, y=80) #places label at these pixels

            self.loadingLabel["text"] = "Choose game file."  #Changes the label to choose game file when the program is ready to load a game file
            self.loadingLabel.place(x=10, y=80) #places label at these pixels
            main_file = fd.askopenfile()
            file = main_file.readline()
            file = file[:-1]
            cardNums = main_file.readline()
            cardChar = main_file.readlines()
            deck = open(file, "r")
            n = 2
            card_deck = deck.readline()
            cardDeck = ([card_deck[i:i+n] for i in range(0, len(card_deck), n)])
            random.shuffle((cardDeck))
            """
            A old continue button used for testing after loading a file
            self.continueButton= Button(self.root, text="Continue", font=(200), compound="center", borderwidth=0, bg=bgcolour, highlightthickness=0, command=lambda:[self.cont(), self.root.quit, self.root.destroy], width = 80, height= 10)
            self.continueButton.place(x=0, y=0) #places label at these pixels
            """
            self.cont()
            self.root.mainloop()
        except:
            print("Unexpected error")

    def cont(self):
        self.loadingLabel["text"] = "Continuing"  #If user is on a slow pc the loading label should change to continuing, So the user knows something is happening.
        self.loadingLabel.place(x=90, y=70) #places label at these pixels)
        self.root.destroy() #Destroys the small tkinter window
        gameSelector() #Calls the game selector function


  

def gameSelector():
    global cardDeck
    #Creating tkinter window
    root = Tk()
    root.title('Card Games')
    root.geometry('1920x1080')
    root.config(bg=bgcolour)
    padx = 10
    pady = 10
    card = 1
    xAxis = 500
    yAxis = 100

    #labels
    tk.Label(root, text ="Card Games", fg='DarkGreen', bg=bgcolour, font = ("Times New Roman", 50)).grid(column = 2, row = 0, padx = padx, pady = pady)
    tk.Label(root, text = "Card Game :", bg=bgcolour, font = ("Times New Roman", 50)).grid(column = 0, row = 1, padx = padx, pady = pady)

    #Combobox creation
    n = tk.StringVar()
    gameChoosen = ttk.Combobox(root, textvariable = n)
    # Adding combobox drop down list
    gameChoosen['values'] = (' Bridge',' Hearts',' Last Card',' Go Fish',' More to come')  
    gameChoosen.grid(column = 1, row = 1)
    #gameChoosen.current()

    def gameChanged():
        print(gameChoosen.get())

    gameSelectButton = tk.Button(root, text="Select Game", font=(200), compound="center", borderwidth=0, bg='blue', highlightthickness=0, command= gameChoosen.bind('<<ComboboxSelected>>', gameChanged))
    gameSelectButton.grid(column = 1, row = 2, padx = padx, pady = pady)

    while card < len(cardDeck):
        print(cardDeck[card] + ".gif")
        cardImg = Image.open(cardDeck[card] + ".gif")
        cardImg = ImageTk.PhotoImage(cardImg)
        cardImg = tk.Label(root, image=cardImg)
        cardImg.place(x = xAxis)
        cardImg.place(y = yAxis)
        xAxis + 3
        yAxis + 3
        card += 1

    root.mainloop()




#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    gameSelector()
    #load()
    