from tkinter import *
import random
from tkinter import PhotoImage
x,y = (random.randint(100,1100)),(random.randint(100,700))
win = Tk()
win.title("Quig Unshackled")
win.geometry("300x300")
win.geometry("-10+0")
win.wm_attributes('-transparentcolor','#add123')
win.config(bg = '#add123')
image = PhotoImage(file="quig1.png")
win.wm_attributes('-fullscreen', 'True')

image = image.zoom(5, 5)  
image_label = Label(win, image=image)
image_label.place(x=(random.randint(100,1100)),y=(random.randint(100,700)))
win.wm_attributes('-fullscreen', 'True')

win.mainloop()
