import time
import tkinter


def countdown():
    countlabel.configure(background="white")
    howlong = int(textbox.get())
    for i in range(howlong, 0, -1):
        countlabel.configure(text=i)
        window.update()
        time.sleep(1)
    countlabel.configure(text="끝!")


window = tkinter.Tk()
window.geometry("800x600")
window.title("첫 번째 GUI")
window.configure(background="grey")

lbl = tkinter.Label(window, text="몇 초를 카운트다운 하겠습니까?")
lbl.pack()
textbox = tkinter.Entry(window)
textbox.pack()
count = tkinter.Button(window, text="카운트다운!", command=countdown)
count.pack()

countlabel = tkinter.Label(window, height="10", width="10")
countlabel.pack()

window.mainloop()
