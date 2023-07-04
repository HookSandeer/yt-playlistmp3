
#! By Hooksander

import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import Playlist

win = Tk()
win.title("Download Youtube playlist")
win.geometry("1000x300")


def quitter() :
    win.destroy()
    sys.exit()
    return 0
    
def savePath() :
    win = Tk()
    win.withdraw()
    directoryPath = filedialog.askdirectory()
    return directoryPath

def okButton() :
    userEntry = user.get()
    youtubePlaylist = Playlist(userEntry)
    
    playlistName.config(state=NORMAL)
    playlistName.insert("1.0", youtubePlaylist.title)
    playlistName.config(state=DISABLED)
    
    numberVideos.config(state=NORMAL)
    numberVideos.insert("1.0", len(youtubePlaylist.videos))
    numberVideos.config(state=DISABLED)
    

title = Label(win, text="Download Youtube Playlist", font=('Arial', 20)).grid(row=0, column=1)

textLink = Label(win, text="Enter the link of your playlist playlist : ", font=('Arial', 10)).grid(row=1, column=0)
user = Entry(win, width=50)
user.grid(row=1, column=1)
linkValid = Button(win, text="Ok", command=okButton).grid(row=1, column=2)


titlePlaylistName = Label(win, text='Playlist name : ', font=('Arial', 10)).grid(row=2, column=0)

playlistName = Text(win, width=50, height=1, state=DISABLED)
playlistName.grid(row=2, column=1)

titleNumberVideos = Label(win, text="Number of videos : ", font=('Arial', 10)).grid(row=2, column=2)

numberVideos = Text(win, width=3, height=1, state=DISABLED)
numberVideos.grid(row=2, column=3)

titleAsk = Label(win, text="Download it ?", font=('Arial', 10)).grid(row=2, column=4)
buttonYes = Button(win, text="Yes").grid(row=2, column=5)
buttonNo = Button(win, text="No").grid(row=2, column=6)



win.mainloop()