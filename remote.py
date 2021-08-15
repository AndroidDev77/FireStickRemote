from tkinter import *
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect("192.168.0.202", 5555)
device = client.devices()
device = device[0]
print(f'Connected to {device}')

def rewindclicked():
    device.shell('input keyevent 88')

def playclicked():
    device.shell('input keyevent 85')

def fowardclicked():
    device.shell('input keyevent 87')

def upclicked():
    device.shell('input keyevent 19')

def downclicked():
    device.shell('input keyevent 20')

def leftclicked():
    device.shell('input keyevent 21')

def rightclicked():
    device.shell('input keyevent 22')

def enterclicked():
    device.shell('input keyevent 66')
    
def backclicked():
    device.shell('input keyevent 4')

def homeclicked():
    device.shell('input keyevent 3')
    
def menuclicked():
    device.shell('input keyevent 1')

def volupclicked():
    device.shell('input keyevent 24')
 
def voldnclicked():
    device.shell('input keyevent 25')\

def muteclicked():
    device.shell('input keyevent 164')

def onclose():
    client.remote_disconnect()
    window.destroy()
    
window = Tk()
window.title("FireTV Remote")
window.geometry('350x200')
window.protocol("WM_DELETE_WINDOW", onclose)


rewindbtn = Button(window, text="Rewind", command=rewindclicked)
rewindbtn.grid(column=0, row=0)

plybtn = Button(window, text="Play/Pause", command=playclicked)
plybtn.grid(column=1, row=0)

fowardbtn = Button(window, text="Foward", command=fowardclicked)
fowardbtn.grid(column=2, row=0)

upbtn = Button(window, text="Up", command=upclicked)
upbtn.grid(column=1, row=3)

downbtn = Button(window, text="Down", command=downclicked)
downbtn.grid(column=1, row=5)

leftbtn = Button(window, text="Left", command=leftclicked)
leftbtn.grid(column=0, row=4)

enterbtn = Button(window, text="Enter", command=enterclicked)
enterbtn.grid(column=1, row=4)

rightbtn = Button(window, text="Right", command=rightclicked)
rightbtn.grid(column=2, row=4)

backbtn = Button(window, text="Back", command=backclicked)
backbtn.grid(column=0, row=6)

homebtn = Button(window, text="Home", command=homeclicked)
homebtn.grid(column=1, row=6)

menubtn = Button(window, text="Menu", command=menuclicked)
menubtn.grid(column=2, row=6)

voldnbtn = Button(window, text="Vol -", command=voldnclicked)
voldnbtn.grid(column=0, row=7)

mutebtn = Button(window, text="Mute", command=muteclicked)
mutebtn.grid(column=1, row=7)

volupbtn = Button(window, text="Vol +", command=volupclicked)
volupbtn.grid(column=2, row=7)
window.mainloop()

