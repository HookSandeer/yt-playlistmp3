
#! By HookSander

import os
from pytube import Playlist

def userLink():
    var = input("Entrer votre lien de la playloist youtube \n=> ")
    downloadFile = Playlist(var)
    return downloadFile

def download(playlist):
    playlistLen = len(playlist.videos)
    print("Téléchargement de laplaylist : {}\n Nombre de vidéos : {}".format(playlist.title, playlistLen))
    count = 0
    for video in playlist.videos :
        count += 1
        print("Téléchargement de la vidéo {}/{}".format(count, playlistLen))
        file = video.streams.filter(only_audio=True).download()
        base, ext = os.path.splitext(file)
        newFile = base + ".mp3"
        os.rename(file, newFile)
        print("{} a finit de télécharger.".format(video.title))
    print("Téléchargement terminé.")
    

    
if __name__ ==  '__main__' :
    download(userLink())
    input = ("Appuyer sur Entrer pour quiter...")