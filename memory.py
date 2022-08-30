# memory game for platics in waterways / oceans
import turtle
from time import sleep
from random import shuffle


def init():
    global screen, cards
    screen = turtle.Screen()
    screen.title('Memory game match plastic in the ocean to remove')
    screen.bgcolor("CornFlowerBlue")
    sh_names = ["bag.gif", "bottle.gif", "net.gif", "straw.gif"]
    screen.addshape("back.gif")
    screen.addshape("fish.gif")
    for fname in sh_names:
        screen.addshape(fname)
        
    face_up = [False] * 9
    card_type = ["bag", "bottle", "net", "straw"] * 2
    card_type.append("fish")
    shuffle(card_type)
    card_pos = [(-130,-130), (0,-130), (130,-130), (-130,0), (0,0), (130,0), (-130,130), (0,130), (130,130)]
    cards = []
    for num in range(9):
        t = turtle.Turtle()
        t.front = card_type[num]
        t.shape("back.gif")
        t.penup()
        t.goto(card_pos[num])
        sleep(1)
        cards.append(t)
        # cards[num].shape(card_type[num]+".gif")
    writer = turtle.Turtle()
    writer.penup()
    writer.ht()
    for x in range(1,4):
        writer.goto(x * 130 - 260, -225)
        writer.write(x, move=False, align="left", font=("Arial", 18, "normal"))
        writer.goto(-225, x * 130 - 260)
        writer.write(x, move=False, align="left", font=("Arial", 18, "normal"))
    
def get_card():
    global screen, cards
    col = screen.numinput("get column", "Please enter 1 to 3 for column")
    row = screen.numinput("get row", "Please enter 1 to 3 for row")
    card_num = int((row - 1) * 3 + (col - 1))
    cards[card_num].shape(cards[card_num].front + ".gif")
    return cards[card_num].front, card_num

if __name__ == "__main__":
    init()
    card1, card1_num = get_card()
    card2, card2_num = get_card()
    if card1 != card2:
        print("yes")