from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()

class MusicPlayer:
    root.configure(bg = "#fcfcec")
    root.geometry("490x180")
    def __init__(self , window):
        def des():
            mixer.music.stop()
            Load.destroy()
            Play.destroy()
            Pause.destroy()
            Close.destroy()

        window.title('Musice Player') ; window.resizable(0,0)

        Load = Button(window , text = 'Load' , width = 10 , command =
        self.load , bg = 'orange' , fg = '#fcfcec' , font = ('times' , 20))

        Play = Button(window , text = 'Play' , width = 10 , command =
        self.play , bg = 'orange' , fg = '#fcfcec' , font = ('times' , 20))
        
        Pasue = Button(window , text = 'Pasue' , width = 10 , command =
        self.pause , bg = 'orange' , fg = '#fcfcec' , font = ('times' , 20))
        
        Close = Button(window , text = 'Close' , width = 9 , command = 
        root.quit , bg = 'orange' , fg = '#fcfcec' , font = ('times' , 20))
        
        Load.place(x=0,y=20);Play.place(x=150,y=20);Pasue.place(x=310,y=20)
        Close.place(x=150,y=75)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

app= MusicPlayer(root)
root.mainloop()

