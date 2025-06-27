from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("GAME ROCK PAPER AND SCISSOR")
window.configure(background="black")

image_rock1= ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img1.JPG"))
image_paper1= ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img2.JPG"))
image_scissor1= ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img3.JPG"))
image_rock2 = ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img6.JPG"))
image_paper2 = ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img4.JPG"))
image_scissor2 = ImageTk.PhotoImage(Image.open("C:/Users/ommji_mttma5p/OneDrive/Desktop/rpcimg/img5.JPG"))

label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(window,text=0,font=('arial',60,"bold"),fg="red")
player_score = Label(window,text=0,font=('arial',60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indicator = Label(window,font=("arial",40,"bold"),text="PLAYER",bg="orange",fg="blue")
computer_indicator = Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="orange",fg="blue")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

def updateMessage(a):
    final_message['text'] = a

def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)
    
def Player_Update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

def winner_check(p,c):
    if p==c:
        updateMessage("IT'S A TIE ")
    elif p=="rock":
        if c=="paper":
            updateMessage("COMPUTER WINS ")
            Computer_Update()
        else:
            updateMessage("PLAYER WINS ")
            Player_Update()
    elif p=="paper":
        if c=="scissor":
             updateMessage("COMPUTER WINS ")
             Computer_Update()
        else:
            updateMessage("PLAYER WINS ")
            Player_Update()
    elif p== "scsssor":
        if c=="rock":
            updateMessage("COMPUTER WINS ")
            Computer_Update()
        else:
            updateMessage("PLAYER WINS ")
            Player_Update()
    else:
        pass
            
to_select = ["rock","paper","scissor"]

def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a=="rock":
        label_player.configure(image=image_rock1)
    elif a=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)

def restart_game():
    computer_score["text"] = "0"
    player_score["text"] = "0"
    label_player.configure(image=image_scissor1)
    label_computer.configure(image=image_scissor2)
    final_message["text"] = ""

final_message = Label(window,font=("arial",40,"bold"),bg="red",fg="white")
final_message.grid(row=3, column=2)

button_rock = Button(window,width=16,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2, column=2)
button_scissor = Button(window,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2, column=3)
button_restart = Button(window, width=16, height=3, text="RESTART", font=("arial", 20, "bold"),bg="green", fg="white",command=lambda:restart_game()).grid(row=4, column=2)

window.mainloop()