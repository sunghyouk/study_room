import tkinter

window = tkinter.Tk()
window.geometry("800x200")
window.title("첫 번째 GUI")
window.configure(background="grey")

# red = tkinter.Button(window, text="빨강", bg="red")
# red.pack()

# yellow = tkinter.Button(window, text="노랑", bg="yellow")
# yellow.pack()

# green = tkinter.Button(window, text="초록", bg="green")
# green.pack()

# textbox = tkinter.Entry(window)
# textbox.pack()

# colorlabel = tkinter.Label(window, height="10", width="10")
# colorlabel.pack()


def change_color():
    window.configure(background="white")


white = tkinter.Button(window, text="누르세요", command=change_color)
white.pack()

window.mainloop()
