
#! By HookSander

import os
import webbrowser
from pytube import Playlist
from tkinter import *
from tkinter import messagebox
import time
#from changeOutputPath import mainChangePath


gui = Tk()

gui.title("Youtube Downloader")
gui.geometry("800x300")

def openYT():
    webbrowser.open_new("youtube.com")

def displayOutputh():
    global content
    try :
        textFile = open("outputPath.txt","r")
        conten = textFile.read()
        content = conten[:-1]  #! Remove the line break
        if content == "" :
            return ("Not yet set up")
        else :
            return content
    except :
        return ("Not yet set up")


def mainChangePath():
    win = Tk()

    win.title("Change Output Path")
    win.geometry("800x300")

    def changePathLocation():
        try :
            textFile = open("outputPath.txt","w")
        except :
            textFile = open("outputPath.txt","w+")
        
        userNewLocation = userEntry.get("1.0", END)
        textFile.write(userNewLocation)
        textFile.close()
        userEntry.delete("1.0", END)
        info.insert(0, "Saved !")


    title = Label(win, text="Change Output Path :", font=("Arial", 30), bg='white', fg='black')
    title.grid(row=0, column=0)

    mess = Label(win, text="New Output location :", font=('Arial', 15), bg='white', fg='black')
    mess.grid(row=1, column=0)

    userEntry = Text(win, height=1)
    userEntry.grid(row=2, column=0)

    btn = Button(win, text="Valide", command=changePathLocation, height=1, width=5)
    btn.grid(row=2, column=1)

    info = Entry(win, font=('Arial', 10), bg='white', fg='black')
    info.grid(row=3, column=0)

    alert = Label(win, text="You need to restart the application !", font=('Arial', 20), bg='white', fg='red')
    alert.grid(row=4, column=0)

    win.mainloop()

def userLink():         #? Already Edited, no need more
    var = link.get("1.0", END)
    downloadFile = Playlist(var)
    return downloadFile


def console(text):      #! Do not edit
    cons.insert(0, text)

def clear_console():    #! Do not edit
    time.sleep(5)
    cons.delete(0, END)

def audioOrVideo():
    if cb.get() == 1 :
        return 'audio'
    elif cb.get() == 0 :
        return 'video'
    else :
        messagebox.showerror("Warning !", "Something went wrong in audioOrVideo Select !")
        
def saveFile(file):     #TODO => Maybe need to edit, but not sure
    base, ext = os.path.splitext(file)
    newFile = base + '.mp3'
    os.rename(file, newFile)

def download_video(playlist, Upath):
    playlistlen = len(playlist.videos)
    console("Téléchargement de la playlist {}".format(playlist.title))
    count = 0
    for video in playlist.videos :
        count += 1
        file = video.streams.get_highest_resolution()
        outvideo = file.download(Upath)
        return outvideo


    
    
    
    
def download_audio(link) :
    global content
    video = YouTube(link)
    extractAudio = video.streams.filter(only_audio=True).first()
    outAudio = extractAudio.download(output_path=content)
    return outAudio

def download():
    if audioOrVideo() == 'audio' :
        saveFile(download_audio(userLink()))
        console("Download Done !")
    if audioOrVideo() == 'video' :
        download_video(userLink())
        console("Download Done !")
    


title = Label(gui, text="Youtube Download", font=('Arial', 30), bg='white', fg="black")
title.grid(row=0, column=0)

out = Label(gui, text="Current Path :", font=('Arial', 15), bg='white', fg='black')
out.grid(row=1, column=0)

outputPath = Entry(gui, width=70)
outputPath.grid(row=2, column=0)
outputPath.insert(0, displayOutputh())

submitOut = Button(gui, text="Change", command=mainChangePath, height=1, width=5)
submitOut.grid(row=2, column=1)

linkDis = Label(gui, text="Your Link :", font=('Arial', 15), bg='white', fg='black')
linkDis.grid(row=3, column=0)

link = Text(gui, height=1)
link.grid(row=4, column=0)

valide = Button(gui,text="Submit", command=userLink, height=1, width=5)
valide.grid(row=4, column=1)

cb = IntVar()
checkButton = Checkbutton(gui, text="Only Audio (.mp3)(Default : .mp4)", variable=cb, onvalue=1, offvalue=0, command=audioOrVideo)
checkButton.grid(row=5, column=0)

clear_button = Button(gui, text="Clear",command=clear_console, height=1, width=5)
clear_button.grid(row=7, column=1)

download_button = Button(gui, text="Download !", command=download, height=1, width=5)
download_button.grid(row=5, column=1)

indic = Label(gui, text="Satus : ", font=("Arial", 15), bg='white', fg='black')
indic.grid(row=6, column=0)

cons = Entry(gui, font=("Arial", 15), bg='white', fg='black')
cons.grid(row=7, column=0)

alt = Menu(gui)
men = Menu(alt, tearoff=0)
men.add_command(label="Open Youtube", command=openYT)
men.add_command(label="Leave", command=gui.quit)
alt.add_cascade(label="File", menu=men)

gui.config(menu=alt)

gui.mainloop()