
#! By HookSander

import os
from pytube import Playlist

def userLink():
    var = input("Entrer votre lien de la playloist youtube \n=> ")
    downloadFile = Playlist(var)
    return downloadFile

def valide():
    user = input("Voulez vous télécharger cette playlist ? [Y/o]\n=> ").lower()
    if user == 'y' :
        return True
    else :
        return False

def download(playlist):
    playlistLen = len(playlist.videos)
    print("Téléchargement de laplaylist : {}\n Nombre de vidéos : {}".format(playlist.title, playlistLen))
    count = 0
    if valide() :
        for video in playlist.videos :
            count += 1
            print("Téléchargement de la vidéo {}/{}".format(count, playlistLen))
            audioFile = video.streams.filter(only_audio=True).first()
            file = audioFile.download()
            base, ext = os.path.splitext(file)
            newFile = base + ".mp3"
            os.rename(file, newFile)
            print("{} a finit de télécharger.".format(video.title))
        print("Téléchargement terminé.")
    else :
        input("Appuyer sur entrer pour quitter, téléchargement annulé")


    

    
if __name__ ==  '__main__' :
    download(userLink())
    input = ("Appuyer sur Entrer pour quiter...")
    
