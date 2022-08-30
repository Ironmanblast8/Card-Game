import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
from PIL import Image, ImageTk
from os.path import exists

bgcolour = ('lightgreen') #Sets bgcolour as global variable

# main_file = open("bridge1.txt", "r")
# file = main_file.readline()
# file = file[:-1]
# cardNums = main_file.readline()
# cardChar = main_file.readlines()
# deck = open(file, "r")
# n = 2
# cardDeck = deck.readline()
# cardDeck = ([cardDeck[i:i+n] for i in range(0, len(cardDeck), n)])
# random.shuffle((cardDeck))


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
            deck = open(file, "r")
            n = 2
            card_deck = deck.readline()
            cardDeck = ([card_deck[i:i+n] for i in range(0, len(card_deck), n)])
            random.shuffle((cardDeck))
            
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

    # Declaring constrants
    padx = 10
    pady = 10
    card = 0
    buttonRow = 0
    menuRow = 0
    menuCol = 0
    cards = []
    gridSize = 8

    #Sets up the cardGames to play
    cardGames = [' Memory',' Hearts',' Last Card',' Go Fish',' More to come']

    #labels
    tk.Label(root, text ="Card Games", fg='DarkGreen', bg=bgcolour, font = ("Times New Roman", 50)).grid(column = 2, row = 0, padx = padx, pady = pady)
    tk.Label(root, text = "Card Game :", bg=bgcolour, font = ("Times New Roman", 50)).grid(column = 0, row = 1, padx = padx, pady = pady)

    #Combobox creation
    n = tk.StringVar()
    gameChoosen = ttk.Combobox(root, textvariable = n)
    # Adding combobox drop down list using the cardGames list 
    gameChoosen['values'] = (cardGames)  
    gameChoosen.grid(column = 1, row = 1)
    #gameChoosen.current()

    def gameChanged():
        errorWindow = tk.Tk()
        errorWindow.title("Error")
        #print(gameChoosen.get())
        if gameChoosen.get() in cardGames:
            cardGame = gameChoosen.get() #Makes cardgame the gamechoosen
            errorWindow.destroy()
            launchGame(cardGame)
        elif gameChoosen.get() == "":
            label = ttk.Label(errorWindow, text="Blank Card Game, Enter value")
            label.pack(side="top", fill="x", pady=10)
            errorLoad = tk.Button(errorWindow, text="Okay", command = errorWindow.destroy)
            errorLoad.pack()
        else:
            label = ttk.Label(errorWindow, text="Invalid card game try again, Might not exist yet")
            label.pack(side="top", fill="x", pady=10)
            errorLoad = tk.Button(errorWindow, text="Okay", command = errorWindow.destroy)
            errorLoad.pack()
        
        errorWindow.mainloop()

    gameSelectButton = tk.Button(root, text="Select Game", font=(200), compound="center", borderwidth=0, bg='red', highlightthickness=0, command= gameChoosen.bind('<<ComboboxSelected>>', gameChanged))
    gameSelectButton.grid(column = 1, row = 2, padx = padx, pady = pady)
    cardsFrame = tk.Frame(root)
    cardsFrame.grid(rows=1, column=2)
    #print(cardDeck)
    while card < len(cardDeck):
        cardImg = (Image.open(f"cards/{cardDeck[card]}.gif"))
        cardImg = cardImg.resize((108 ,151)) # Halfs the size of the large playing cards. For the loading screen this is cause we don't need it to be large
        cardImg = ImageTk.PhotoImage(cardImg)
        cards.append(cardImg)
        card += 1
        button=tk.Button(cardsFrame, image=cardImg, command=lambda:  print(cardImg))
        if buttonRow < gridSize:
            button.grid(row=menuRow,column=menuCol)
            buttonRow += 1
            menuCol += 1
        if buttonRow == gridSize:
             menuRow += 1        
             buttonRow = 0
             menuCol = 0
 
    root.mainloop()
    
def launchGame(cardGame):
    loadGame = cardGame.replace(" ", "").lower()
    if exists(loadGame+".py"):
        exec(open(loadGame+".py").read())
    else:
        errorWindow = tk.Tk()
        label = ttk.Label(errorWindow, text="Card game doesn't exist yet, Maybe add it?")
        label.pack(side="top", fill="x", pady=10)
        errorLoad = tk.Button(errorWindow, text="Okay", command = errorWindow.destroy)
        errorLoad.pack()
        errorWindow.mainloop()

#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    #gameSelector()
    load()