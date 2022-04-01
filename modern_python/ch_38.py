import random
import tkinter


# 1. 플레이어 클래스
class Player(object):
    def __init__(self, canvas, color):
        self.color = color
        size = random.randint(1, 100)
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 700)
        x2 = x1 + size
        y2 = y1 + size
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords, tags=color)
        canvas.itemconfig(self.piece, fill=color)

    def move(self, direction):
        if direction == 'u':
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'd':
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == 'l':
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'r':
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)


# 2. 이벤트 핸들러 함수 만들기
def handle_key(event):
    if event.char == 'w':
        player1.move("u")
    if event.char == 's':
        player1.move("d")
    if event.char == 'a':
        player1.move("l")
    if event.char == 'd':
        player1.move("r")
    if event.char == 'i':
        player2.move("u")
    if event.char == 'k':
        player2.move("d")
    if event.char == 'j':
        player2.move("l")
    if event.char == 'l':
        player2.move("r")

    yellow_xy = canvas.bbox(1)
    overlapping = canvas.find_overlapping(
        yellow_xy[0], yellow_xy[1], yellow_xy[2], yellow_xy[3]
    )
    if 2 in overlapping:
        canvas.create_text(100, 100, font=("Arial", 20), text="Tag!")


# 3. 창과 위젯 초기화하기
window = tkinter.Tk()
window.geometry("800x800")
window.title("태그!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')

player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")
canvas.bind_all('<Key>', handle_key)

window.mainloop()
