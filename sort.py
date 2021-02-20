#made by LordQuerix <3
import os
import string
import time
import glob
from os import path
import shutil
import sys
import time
from time import sleep

#check if modules are installed
try:
    f= open("installed.ini")
except IOError:
    f= open("installed.ini","w+")
finally:
    f= open("installed.ini", "r")
filetext= f.readline()


#install modules
if filetext != "installed components":
    print("")
    print("the first run will install the necessary components! if you don't have one, the script will either crash or end with an error after a while, it's best to restart the script after installing the components!")
    print("")
    input("ready to install?(do not type anythink just click enter!):")
    print("")
    os.system("pip install configparser")
    os.system("pip install glob")
    os.system("pip install shutil")
    f= open("installed.ini", "a")
    f.write("installed components")
    f.close()
    print("installed components, rerun the script")
    sys.exit()

#import configparser and check for settings.ini
import configparser
Config = configparser.ConfigParser()
try:
    f= open("settings.ini")
except IOError:
    f= open("settings.ini","w+")
finally:
    f= open("settings.ini", "r")
filetext= f.readline()

if filetext == "":
    f = open("settings.ini","a")
    pathforwrite = os.path.dirname(os.path.abspath(__file__))
    f.write("[path]\npath=%s\*\ndocpath=%s\documents\nmusicpath=%s\music\nimgpath=%s\images\nexecpath=%s\executables\nvideopath=%s\Videos\ntorrentpath=%s\Torrents\nrarpath=%s\WinrarFiles\njarpath=%s\jar\ngimppath=%s\gimpprojects\npresentationspath=%s\presentations\nscriptspath=%s\scripts\ndllpath=%s\dlls\nisopath=%s\iso\notherpath=%s\others\n[images]\nfile_name=images\nextensions=.jpg .png .bmp .JPG .PNG .BMP\n[documents]\nfile_name=documents\nextensions=.doc .txt .docx .pdf .json .csv\n[music]\nfile_name=music\nextensions=.mp3 .wav .ogg .wov\n[video]\nfile_name=videos\nextensions=.mp4 .avi .mov .mkv .ts\n[torrent]\nfile_name=torrents\nextensions=.torrent\n[Winrar]\nfile_name=winrarfiles\nextensions=.rar .zip .7zip .7z\n[exec]\nfile_name=executables\nextensions=.exe .msi\n[jar]\nfile_name=jar\nextensions=.jar .java\n[gimp]\nfile_name=gimp\nextensions=.xcf\n[presentations]\nfile_name=presentations\nextensions=.pptx\n[iso]\nextensions=.iso\n[scripts]\nextensions=.lua .LUA .CT .ct .sk .SK\n[dll]\nextensions=.dll .DLL\n[others]\nextensions=.sfk .SFK .nfo .COM .rmskin" % (pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite,pathforwrite))
    print("settings.ini file created, rerun the script")
    sys.exit()
Config.read("settings.ini")
sections = Config.sections()
sections_count = len(sections)

def Convert(string):
    li = list(string.split(" "))
    return li

#print mini gui xd
os.system('cls')
os.system('color 0a')
print("#########################")
print("#    automatic sorter   #")
print("#        v1.0.0         #")
print("#     By LordQuerix     #")
print("#########################")
print("")
print("Hello! thanks for using my script! The script will automatically sort your files, \nif a file is not sorted, add its extension in the settings.ini file. If you want to rename a file, change it from e.g. \ndocpath=C:\File-sorter\documents to docpath=C:\File-sorter\OTHER_NAME \nMore information on the github page!")
print("")
odp=input("y - sort | n - exit: ")

if odp == "n":
    os.system('cls')
    os.system('color 07')
    exit()
elif odp != "n" and odp != "y":
    print("entered wrong leater, rerun script if you want to do it again")
    os.system('color 07')
elif odp == "y":
    print("Sorting...")
#extensions
documentssettings = Convert(Config.get('documents', 'extensions'))
musicsettings = Convert(Config.get('music', 'extensions'))
picturessettings = Convert(Config.get('images', 'extensions'))
torrentsetting = Convert(Config.get('torrent','extensions'))
videosetting = Convert(Config.get('video','extensions'))
rarsettings = Convert(Config.get('Winrar','extensions'))
execsettings = Convert(Config.get('exec','extensions'))
jarsettings = Convert(Config.get('jar','extensions'))
gimpsettings = Convert(Config.get('gimp','extensions'))
othersettings = Convert(Config.get('gimp','extensions'))
presentationssettings = Convert(Config.get('presentations','extensions'))
isosettings = Convert(Config.get('iso','extensions'))
dllsettings = Convert(Config.get('dll','extensions'))
othersettings = Convert(Config.get('others','extensions'))
scriptssettings = Convert(Config.get('scripts','extensions'))
#path
filename=glob.glob(Config.get('path', 'path'))

#files
DocumentsLocation=Config.get('path', 'docpath')
MusicLocation=Config.get('path', 'musicpath')
ImgLocation=Config.get('path', 'imgpath')
VideoLocation=Config.get('path', 'videopath')
TorrentLocation=Config.get('path', 'torrentpath')
Winrarlocation=Config.get('path', 'rarpath')
execlocation=Config.get('path', 'execpath')
jarlocation=Config.get('path', 'jarpath')
gimplocation=Config.get('path', 'gimppath')
presentationslocation=Config.get('path', 'presentationspath')
isolocation=Config.get('path', 'isopath')
dlllocation=Config.get('path', 'dllpath')
otherlocation=Config.get('path', 'otherpath')
scriptlocation=Config.get('path', 'scriptspath')

#sortingcount
allsortedfiles = 0
#making directories and sorting
for file in filename:
    #doc
    if os.path.splitext(file)[1] in documentssettings:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
            allsortedfiles +=1
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
            allsortedfiles +=1
    #img
    if os.path.splitext(file)[1] in picturessettings:
        if(path.exists(ImgLocation)):
            shutil.move(file,ImgLocation)
            allsortedfiles +=1
        else:
            os.mkdir(ImgLocation)
            shutil.move(file,ImgLocation)
            allsortedfiles +=1

    #music
    if os.path.splitext(file)[1] in musicsettings:
        if(path.exists(MusicLocation)):
            shutil.move(file,MusicLocation)
            allsortedfiles +=1
        else:
            os.mkdir(MusicLocation)
            shutil.move(file,MusicLocation)
            allsortedfiles +=1
    #video
    if os.path.splitext(file)[1] in videosetting:
        if(path.exists(VideoLocation)):
            shutil.move(file,VideoLocation)
            allsortedfiles +=1
        else:
            os.mkdir(VideoLocation)
            shutil.move(file,VideoLocation)
            allsortedfiles +=1
    #torrent
    if os.path.splitext(file)[1] in torrentsetting:
        if(path.exists(TorrentLocation)):
            shutil.move(file,TorrentLocation)
            allsortedfiles +=1
        else:
            os.mkdir(TorrentLocation)
            shutil.move(file,TorrentLocation)
            allsortedfiles +=1
    #winrar
    if os.path.splitext(file)[1] in rarsettings:
        if(path.exists(Winrarlocation)):
            shutil.move(file,Winrarlocation)
            allsortedfiles +=1
        else:
            os.mkdir(Winrarlocation)
            shutil.move(file,Winrarlocation)
            allsortedfiles +=1
    #exec
    if os.path.splitext(file)[1] in execsettings:
        if(path.exists(execlocation)):
            shutil.move(file,execlocation)
            allsortedfiles +=1
        else:
            os.mkdir(execlocation)
            shutil.move(file,execlocation)
            allsortedfiles +=1
    #jar
    if os.path.splitext(file)[1] in jarsettings:
        if(path.exists(jarlocation)):
            shutil.move(file,jarlocation)
            allsortedfiles +=1
        else:
            os.mkdir(jarlocation)
            shutil.move(file,jarlocation)
            allsortedfiles +=1
    #gimp
    if os.path.splitext(file)[1] in gimpsettings:
        if(path.exists(gimplocation)):
            shutil.move(file,gimplocation)
            allsortedfiles +=1
        else:
            os.mkdir(gimplocation)
            shutil.move(file,gimplocation)
            allsortedfiles +=1
    #presentations
    if os.path.splitext(file)[1] in presentationssettings:
        if(path.exists(presentationslocation)):
            shutil.move(file,presentationslocation)
            allsortedfiles +=1
        else:
            os.mkdir(presentationslocation)
            shutil.move(file,presentationslocation)
            allsortedfiles +=1
    #other
    if os.path.splitext(file)[1] in othersettings:
        if(path.exists(otherlocation)):
            shutil.move(file,otherlocation)
            allsortedfiles +=1
        else:
            os.mkdir(otherlocation)
            shutil.move(file,otherlocation)
            allsortedfiles +=1
    #dll
    if os.path.splitext(file)[1] in dllsettings:
        if(path.exists(dlllocation)):
            shutil.move(file,dlllocation)
            allsortedfiles +=1
        else:
            os.mkdir(dlllocation)
            shutil.move(file,dlllocation)
            allsortedfiles +=1
    #iso
    if os.path.splitext(file)[1] in isosettings:
        if(path.exists(isolocation)):
            shutil.move(file,isolocation)
            allsortedfiles +=1
        else:
            os.mkdir(isolocation)
            shutil.move(file,isolocation)
            allsortedfiles +=1
    #scripts
    if os.path.splitext(file)[1] in scriptssettings:
        if(path.exists(scriptlocation)):
            shutil.move(file,scriptlocation)
            allsortedfiles +=1
        else:
            os.mkdir(scriptlocation)
            shutil.move(file,scriptlocation)
            allsortedfiles +=1
print("Done, sorted %s files" % (allsortedfiles))
sleep(3)
os.system('cls')
os.system('color 07')
