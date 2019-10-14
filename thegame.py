from tkinter import *
from random import randrange as rnd, choice, random
import time
import math as m


root = Tk()  # создаем корневое окно 800*600 пикселей
root.geometry('800x600') 

canv = Canvas(root, bg='white')  # Создаем холст
canv.pack(fill=BOTH, expand=1)
canv.create_rectangle(800, 0, 750, 30)

colors = ['red','orange','yellow','green','blue']  # Массив цветов, используемых в программе
	

V = 5  # коэффициент величины скорости
 # функции появления шаров
def new_ball_1():
    global x1, y1, r1, c1
    x1 = rnd(100, 700)
    y1 = rnd(100, 500)
    r1 = rnd(30, 50)
    c1 = choice(colors)
    global o1
    o1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=c1, width=0)

def new_ball_2():
   global x2,y2,r2,c2
   x2 = rnd(100, 700)
   y2 = rnd(100, 500)
   r2 = rnd(30, 50)
   c2 = choice(colors)
   global o2
   o2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=c2, width=0)

def new_ball_3():
    global x3,y3,r3, c3
    x3 = rnd(100, 700)
    y3 = rnd(100, 500)
    r3 = rnd(30, 50)
    c3 = choice(colors)
    global o3
    o3 = canv.create_oval(x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill=c3, width=0)

 # функция движения
def move(object, x, y, r, c, v_x, v_y):
	canv.delete(object)
	y += v_y
	x += v_x
	obj = canv.create_oval(x - r, y - r, x + r, y + r, fill=c, width=0)
	if x + r >= 800 or x - r <= 0:
		v_x *= (-1)
		v_y = 5*(random() - 0.5)
		x += v_x
	if y + r >= 600 or y - r <= 0:
		v_y *= (-1)
		v_x = 5*(random() - 0.5)
		y += v_y

	return obj, x, y, v_x, v_y

 # функция счета очков
z1, z2, z3 = 0, 0, 0
def count(event, txt):
	global z1, z2, z3
	if (event.x - x1)**2 + (event.y - y1)**2 < r1**2:
		z1 += 1
	if (event.x - x2)**2 + (event.y - y2)**2 < r2**2:
		z2 += 1
	if (event.x - x3)**2 + (event.y - y3)**2 < r3**2:
		z3 += 1
	canv.delete('text')
	canv.create_text(775, 15, text=txt, tag='text')

# процесс запуска count

def click(event):
	count(event, z1 + z2 + z3 + 1)

def f1(event):
	f2(event)

def f2(event):
	f3(event)

def f3(event):
	click(event)

# просто потому, что можем

canv.bind('<Button-1>', f1)


v_x1, v_x2, v_x3 = V * (random() - 0.5), V * (random() - 0.5), V * (random() - 0.5)
v_y1, v_y2, v_y3 = V * (random() - 0.5), V * (random() - 0.5), V * (random() - 0.5)
new_ball_1()
new_ball_2()
new_ball_3()
while True:
	o1, x1, y1, v_x1, v_y1 = move(o1, x1, y1, r1, c1, v_x1, v_y1)
	o2, x2, y2, v_x2, v_y2 = move(o2, x2, y2, r2, c2, v_x2, v_y2)
	o3, x3, y3, v_x3, v_y3 = move(o3, x3, y3, r3, c3, v_x3, v_y3)
	root.update()
	time.sleep(0.013)




