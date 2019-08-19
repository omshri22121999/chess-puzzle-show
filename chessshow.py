import chess.pgn
import chess.svg
import re
import chess
import tkinter
import io
import json
import os
import PIL.Image
import PIL.ImageTk
import cairosvg

pgn = open('./puzzles.pgn')

pgn_data = []

game = 1

while(game!=None):
    game = chess.pgn.read_game(pgn)
    if(game!=None):
        data = {}
        data["Text"] = game.headers["Black"]+" "+game.headers["White"]
        data["FEN"] = game.headers["FEN"].split(" ")[0]
        pgn_data.append(data)    

i=0

window = tkinter.Tk()
window.title("Chess Show")
head = tkinter.Label(window,text = "Problem #"+str(i+1),font=("Arial Bold", 30))

head.grid(column=1,row=0)

svg_img = chess.svg.board(board=chess.Board(pgn_data[i]["FEN"]))
png_img = cairosvg.svg2png(bytestring = svg_img)
im = PIL.Image.open(io.BytesIO(png_img))
photo = PIL.ImageTk.PhotoImage(im)

img = tkinter.Label(window,image = photo,text = pgn_data[i]["Text"])

img.grid(column=1,row=1)

def prev_comm():
    global i
    if(i>0):
        i-=1
        head["text"] = "Problem #"+str(i+1)
        svg_img = chess.svg.board(board=chess.Board(pgn_data[i]["FEN"]))
        
        png_img = cairosvg.svg2png(bytestring = svg_img)
        im = PIL.Image.open(io.BytesIO(png_img))
        photo = PIL.ImageTk.PhotoImage(im)
        img.configure(image=photo)
        img.image = photo
        img['text'] = pgn_data[i]["Text"]

def next_comm():
    global i
    if(i<len(pgn_data)-1):
        i+=1
        head["text"] = "Problem #"+str(i+1)
        svg_img = chess.svg.board(board=chess.Board(pgn_data[i]["FEN"]))
        
        png_img = cairosvg.svg2png(bytestring = svg_img)
        im = PIL.Image.open(io.BytesIO(png_img))
        photo = PIL.ImageTk.PhotoImage(im)
        img.configure(image=photo)
        img.image = photo
        img['text'] = pgn_data[i]["Text"]


prev_b = tkinter.Button(window,command = prev_comm,text = "Prev",height = 3,width = 9)

prev_b.grid(column=0,row=2)


next_b = tkinter.Button(window,command = next_comm,text = "Next",height = 3,width = 9)

next_b.grid(column=2,row=2)
window.mainloop()
