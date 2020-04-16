
# подключение библиотек
from tkinter import *
from time import sleep
from random import randint

# настройка окна
window = Tk()
window.title("Астероид 1.0")
image = Canvas(window, width=600, height=600, bg="#222235")
image.pack()

game = True

moveLeft = False
moveRight = False

x = 300
y = 500
speed =7

aX = 100
aY = 100
aSpeed = 15

stars = {
    "x": [randint(0,600) for i in range(500)],
    "y": [randint(0,600) for i in range(500)],
    "s": [randint(1,4) for i in range(500)]
}

# анализ клавиатуры
def keyDown(event):
    global moveLeft, moveRight
    key = event.keycode
    #print(key)
    if key == 113: moveLeft = True
    if key == 114: moveRight = True
def keyUp(event):
    global moveLeft, moveRight
    key = event.keycode
    #print(key)
    if key == 113: moveLeft = False
    if key == 114: moveRight = False

# связь клавиатуры с функциями
window.bind("<KeyPress>", keyDown)
window.bind("<KeyRelease>", keyUp)

# цикл анимации
while game:
    # анализ действий
    if moveLeft: x -= speed
    if moveRight: x += speed
    if x < 50: x = 50
    if x > 550: x = 550
    aY += aSpeed # двигает астероид вниз
    if aY > 650: # перебрасывает астероид вверх
        aY = -50
        aX = randint(50, 550)
    if aX+50 > x-50 and aX-50 < x+50 and aY+50 > y-50 and aY-50 < y+50:
        game = False
    # звёздочки
    for i in range(len(stars["x"])):
        stars["y"][i] += stars["s"][i]
        if stars["y"][i] > 600:
            stars["y"][i] = 0
            stars["x"][i] = randint(0, 600)
    # отрисовка
    image.delete("all")
    # звёздочки
    for i in range(len(stars["x"])):
        image.create_oval(stars["x"][i]-stars["s"][i],stars["y"][i]-stars["s"][i], stars["x"][i]+stars["s"][i],stars["y"][i]+stars["s"][i], fill="#ffffff", width=0)
        
    # корабль
    color = "#f"+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+"00"
    image.create_polygon(x-30,y+randint(30,50), x-10,y+randint(30,50), x+10,y+150, x-50,y+150, fill=color)
    image.create_polygon(x+30,y+randint(30,50), x+10,y+randint(30,50), x-10,y+150, x+50,y+150, fill=color)
    image.create_polygon(x,y-50, x-50,y+50, x-10,y+40, x,y+50, x+10,y+40, x+50,y+50, fill='#aaaaaa')
    image.create_polygon(x,y-40, x-10,y-20, x,y-10, x+10,y-20, fill='#8888ff')
    image.create_polygon(x-20,y+20, x-10,y+30, x-10,y+50, x-30,y+50, x-30,y+30, fill='#888888')
    image.create_polygon(x+20,y+20, x+10,y+30, x+10,y+50, x+30,y+50, x+30,y+30, fill='#888888')
    image.create_polygon(x-10,y-10, x,y, x+10,y-10, x,y+40, fill='#999999')
    # астероид
    image.create_oval(aX-50, aY-50, aX+50, aY+50, fill="#a83a00", width=0)
    image.create_oval(aX-40, aY-40, aX+20, aY-5, fill="#d17900", width=0)
    image.update()
    sleep(0.01)
window.destroy()
