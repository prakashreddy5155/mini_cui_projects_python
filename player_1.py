
import os
from pygame import mixer 

def dir_printing(data):
    print()
    print("contents present in this directory are :")
    print("↓")
    print()
    for i in data:
        print(i)



mixer.init()

def songcontrolling(selecting_song):
    mixer.music.load("./"+selecting_song)
    mixer.music.play()

    while(True):
        inp = input("Enter 'pause' to pause the song\nEnter 'resume' to resume the song\nEnter 'stop' to stop the song\nEnter 'start' to start the song\nEnter 'goback' to move to the previous directory\nEnter 'absolute_path' to move to a specific folder in this pc\nEnter 'listen' to listen to the songs in the same location : ")

        def dir_printing(data):
            print()
            for i in data:
                print(i)
            print()

        print()
        if(inp.lower() == 'pause'):
            mixer.music.pause()
        elif(inp.lower() == 'resume'):
            mixer.music.unpause()
        elif(inp.lower() == 'stop'):
            mixer.music.stop()
        elif(inp.lower() == 'start'):
            mixer.music.load("./"+ selecting_song)
            mixer.music.play()
        elif(inp.lower() == 'goback'):
            os.chdir("..")
            path = os.listdir()
            dir_printing(path)
            print(f"Now you are in \n{os.getcwd()} Path ")
        elif(inp.lower() == 'listen'):
            val = os.listdir()
            dir_printing(val)
            inp = input("Enter the song name to play : ").lower()
            if(inp.endswith('.mp3') or inp.endswith('.wav')):
                mixer.music.load("./"+inp)
                mixer.music.play()
                selecting_song = inp
            else:
                print()
                print("U did not enter a song  !")
                print()
                10/0
        elif(inp.lower() == 'absolute_path'):
            print()

            print("Songs path is 'D:\python_lang\projects_mini\cli_music_player'" )
            usr_input = input("Enter the path you want to jump into : ")
            os.chdir(usr_input)
            print(f"Now you are in \n {os.getcwd()} Path")
            main()


            
            
    



def main():
    path = os.getcwd()
    os.chdir(path)
    dir_data = os.listdir() 
    dir_printing(dir_data)
    # print() -> Inorder to have better user experience 
    print()
    selecting_directory = input("Enter a Folder name which are displayed above to jump into it: ")
    try: 
        os.chdir(selecting_directory)
        data = os.listdir()
        dir_printing(data)
        print()
    except:
        print("You have entered an invalid Directory name")

    try:
        selecting_song = input("Enter the song name to play the song: ")
        songcontrolling(selecting_song)
    except:
        print("You have entered an Invalid song name")


if(__name__ == "__main__"):
    main()

