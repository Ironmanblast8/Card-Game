#Import the libraries - Note pil is 3rd Party.
import random  # Random shuffles list (Deck of cards)
import tkinter as tk  # Importing tkinter for tkobjects
from tkinter import *
from tkinter import filedialog as fd  # Lets users load files
from tkinter import ttk
from PIL import Image, ImageTk

bgcolour = "lightblue"  # Sets bgcolour as global variable so that multiple classes/methods can use it.

# Settings for the card game
def settings():
    # Creating tkinter window
    root = Tk()
    root.title("Card Game - Settings")
    root.geometry("960x1080")
    root.config(bg=bgcolour)
    #Settings Load method.
    def settingsLoad():
        try:
            # Grabs the entry of the
            hands = int(entry.get())
            numCards = int(entryNum.get())
            numDecks = int(entryDeck.get())
            # If any of the boxes aren't greater then 0 It will forcibly cause a value error to occur.
            if 0 >= hands:
                int("two")
            if 0 >= numCards:
                int("two")
            if 0 >= numDecks:
                int("two")

            # If no errors in the settings load closes the menu and calls the play method
            root.destroy()
            play(hands, numCards, numDecks)
        except ValueError:
            errorScreen = Toplevel(root)
            errorScreen.geometry("1235x200")
            errorScreen.title("Error Window")
            errorScreen.config(bg="red")
            #Creates a label saying enter integer value
            Label(
                errorScreen,
                text="Please enter integer value into settings",
                bg="red",
                font=("Courier 38 bold"),
            ).grid(column=0, row=1, sticky=EW)
            #Creates a label saying enter positive value
            Label(
                errorScreen,
                text="Might need to also be a positive integer",
                bg="red",
                font=("Courier 15 bold"),
            ).grid(column=0, row=2, sticky=S)

    # Initialize a Label
    label = Label(root, text="Hands to play:", bg=bgcolour, font=("Courier 22 bold"))
    label.pack()

    # Create an Entry widget to accept User Input
    entry = Entry(root, width=40)
    entry.focus_set()
    entry.pack()

    # Initialize a Label
    label = Label(
        root, text="Amount of Cards in a hand:", bg=bgcolour, font=("Courier 22 bold")
    )
    label.pack()

    # Create an Entry widget to accept User Input
    entryNum = Entry(root, width=40)
    entryNum.focus_set()
    entryNum.pack()

    # Initialize a Label
    label = Label(root, text="Number of decks:", bg=bgcolour, font=("Courier 22 bold"))
    label.pack()

    # Create an Entry widget to accept User Input
    entryDeck = Entry(root, width=40)
    entryDeck.focus_set()
    entryDeck.pack()

    # Create a Button to validate Entry Widget, Then calls the settings load method to make sure teh settings are correct.
    button = ttk.Button(root, text="Enter Settings", width=100, command=settingsLoad)
    button.pack()

    # Loops the windows so it doesn't close on it
    root.mainloop()


# The play method is passed the values from the settings method
def play(hands, numCards, numDecks):
    # print(hands)
    # print(numCards)
    # print(numDecks)

    # Creating tkinter window with a screen of 500x250
    root = tk.Tk()
    root.title("Card Games")
    root.geometry("500x250")
    root.config(bg=bgcolour)

    loadingLabel = tk.Label(
        root, text="Loading...", bg=bgcolour, font=("verdana", 40), fg="black"
    )  # If user is on a slow pc the loading label should say loading, So the user knows something is happening.
    loadingLabel.place(x=100, y=80)  # Places label at these pixels
    loadingLabel[
        "text"
    ] = "Choose game file."  # Changes the label to choose game file when the program is ready to load a game file
    loadingLabel.place(x=10, y=80)  # Places label at these pixels

    main_file = fd.askopenfile()
    file = (
        main_file.readline()
    )  # Reads the first line in the file to then load in the text file of the deck hand.
    file = file[:-1]
    # numberCards = main_file.readline()
    deck = open(file, "r")
    n = 2 #Constant 2 as that's the key for each character
    card_deck = deck.readline()
    cardDeck = [card_deck[i : i + n] for i in range(0, len(card_deck), n)] * numDecks
    # print(cardDeck) # Makes sure it's shuffled
    random.shuffle(cardDeck)  # Shuffles the cardDeck list.
    # Compresses the carDeck list into a string so you can split it up into hands.
    cardDeckStr = " ".join([str(elem) for elem in cardDeck])
    cardDeckStr = cardDeckStr.replace(" ", "") # Removes the spaces between the characters
    # Seperates the cards based on amount of cards and hands
    cardHandDecks = [
        cardDeckStr[i * numCards * n : (i * numCards * n) + numCards * n]
        for i in range(hands)
    ] 
    # print(cardDeck)
    # print(cardDeckStr)
    # print(cardHandDecks)
    root.destroy()

    # Creating tkinter window of the game, We have to re create it as we destroyed the previous one.
    root = tk.Tk()
    root.title("Card Game")
    root.geometry("1920x1080")
    root.config(bg=bgcolour)

    # Variables
    cardsFrame = tk.Frame(root, bg=bgcolour)
    cardsFrame.grid(rows=1, column=2)
    gridSize = 10  # Sets the grid size so cards only go 10 cards across.
    handsDealt = 0
    handRow = 0

    # Will display the hand of cards
    def sel(i):  # Changes the label to tell user what hand is showing.
        buttonRow = 0
        menuRow = 0
        menuCol = 0
        player = i - 1
        card = 0
        handLabel.set("You've selected the hand number " + str(i))

        # print(cardDeckStr)
        while card < numCards:
            try:
                # print(player)
                localCardHandDecks = [
                    cardHandDecks[player][x : x + n]
                    for x in range(0, len(cardHandDecks[player]), n)
                ]
                # print(localCardHandDecks)
            except IndexError:
                # Prints the error
                print(IndexError)
                pass
            cardImg = Image.open(f"cards/{localCardHandDecks[card]}.gif")
            cardImg = cardImg.resize(
                (108, 151)
            )  # Half's the size of the large playing cards. For the loading screen this is cause we don't need it to be large3
            cardImg = ImageTk.PhotoImage(cardImg)
            cardImg.im = cardImg
            card += 1
            button = tk.Button(
                cardsFrame, image=cardImg, command=lambda i=card: print(i), bg=bgcolour
            )
            # Makes it so the cards move up to the side by ten and then go to next if statement
            if buttonRow < gridSize:
                button.grid(row=menuRow, column=menuCol)
                buttonRow += 1
                menuCol += 1
            # When button row = gridsize default 10 it will more the row down by 1 then display another 10 cards adn so on.
            if buttonRow == gridSize:
                menuRow += 1
                buttonRow = 0
                menuCol = 0  # Resets menuCol to its default of 0

    while handsDealt < hands:
        handsDealt += 1  # Adds one to handsDealt
        handLabel = StringVar()
        # Creates a label widget
        tk.Label(root, textvariable=handLabel).grid(row=0, column=11)
        # Creates label asking what hand does user want to display
        handLabel.set("What hand do you want to display?")
        # Changes the radio button depending on the number of what hand
        handsButton = Radiobutton(
            root,
            text="Show hand " + str(handsDealt),
            value=handsDealt,
            command=lambda i=handsDealt: sel(i),
        )
        # Moves the button in the grid through each loop of the while
        handsButton.grid(row=1 + handRow, column=11)
        handRow += 1

    root.mainloop()

# If the name of the program is called main it will run everything below.
if __name__ == "__main__":
    settings()  # Runs the settings method
