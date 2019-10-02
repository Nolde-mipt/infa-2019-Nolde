#!/usr/bin/env python3
from graph import polygon, rectangle, circle
from graph import penColor, brushColor
from graph import canvasSize, windowSize
from graph import run
import math


xf1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xf2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xf3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xf4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xf5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xf6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yf6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# объявление массивов, которые подаются на вход функции polygon для рисования скругленных участков


def bird(xb, yb, mb):
    polygon([(xb, yb), (xb - 5 * mb, yb), (xb - 10 * mb, yb - 1 * mb), (xb - 15 * mb, yb - 2 * mb),
             (xb - 20 * mb, yb - 3.5 * mb), (xb - 25 * mb, yb - 6 * mb),
             (xb - 30 * mb, yb - 9 * mb), (xb - 35 * mb, yb - 12.5 * mb),
             (xb - 37.5 * mb, yb - 15 * mb), (xb - 40 * mb, yb - 20 * mb),
             (xb - 30 * mb, yb - 20 * mb), (xb - 20 * mb, yb - 18 * mb),
             (xb - 10 * mb, yb - 15 * mb), (xb - 5 * mb, yb - 13 * mb),
             (xb, yb - 10 * mb), (xb + 3.5 * mb, yb - 8 * mb),
             (xb + 5 * mb, yb - 10 * mb), (xb + 7 * mb, yb - 13 * mb),
             (xb + 10 * mb, yb - 16 * mb), (xb + 15 * mb, yb - 18.5 * mb),
             (xb + 20 * mb, yb - 20 * mb), (xb + 30 * mb, yb - 22 * mb), (xb + 40 * mb, yb - 20 * mb)
             ])
# рисует птицу с координатами нижней точки xb, yb и масштабированием mb


def points_filling():
    for i1 in range(0, 15):
        xf1[i1] = 35 + 15 * i1
        yf1[i1] = (- xf1[i1] ** 2.95) * 0.00001 + 190
    for i2 in range(0, 21):
        xf2[i2] = 615 + 5 * i2
        yf2[i2] = math.sin(math.pi / 85 * xf2[i2] - 21.16) * 75 / 2 + 88
    for i3 in range(0, 11):
        xf3[i3] = 25 + 10 * i3
        yf3[i3] = 0.02727 * xf3[i3] ** 2 - 4.0909 * xf3[i3] + 349.77
    for i4 in range(0, 12):
        xf4[i4] = 520 + 10 * i4
        yf4[i4] = math.sin(math.pi / 235 * xf4[i4] - 3.58) * 65 + 265
    for i5 in range(0, 10):
        xf5[i5] = 365 + 10 * i5
        yf5[i5] = math.sin(-math.pi / 450 * xf5[i5] + 4.71) * 350 / 2 + 300
    for i6 in range(0, 14):
        xf6[i6] = 675 + 25 * i6
        yf6[i6] = math.sin(math.pi / 275 * xf6[i6] - 6.71) * 170 / 2 + 377
# заполняет массивы, подаваемые на вход функции polygon для рисования скругленных участков


def backstage():
    penColor(255, 204, 153)
    brushColor(255, 204, 153)
    rectangle(0, 0, 1000, 100)
    penColor(255, 229, 204)
    brushColor(255, 229, 204)
    polygon([(0, 100), (1000, 100), (1000, 215), (0, 200)])
    penColor(255, 255, 153)
    brushColor(255, 255, 153)
    polygon([(0, 200), (1000, 215), (1000, 300), (0, 350)])
    penColor(188, 143, 143)
    brushColor(188, 143, 143)
    polygon([(0, 350), (1000, 300), (1000, 500), (0, 500)])
# рисует фон


def mtn_line1():
    penColor(225, 153, 51)
    brushColor(255, 153, 51)
    polygon([(1000, 160), (10, 225), (20, 185), (xf1[0], yf1[0]),
             (xf1[1], yf1[1]), (xf1[2], yf1[2]), (xf1[3], yf1[4]),
             (xf1[5], yf1[5]), (xf1[6], yf1[6]), (xf1[7], yf1[7]),
             (xf1[8], yf1[8]), (xf1[9], yf1[9]), (xf1[10], yf1[10]),
             (xf1[11], yf1[11]), (xf1[12], yf1[12]), (xf1[13], yf1[13]),
             (xf1[14], yf1[14]), (325, 100), (350, 125), (435, 175), (490, 165),
             (515, 180), (565, 130), (595, 140), (615, 125), (xf2[0], yf2[0]),
             (xf2[1], yf2[1]), (xf2[2], yf2[2]), (xf2[3], yf2[3]),
             (xf2[4], yf2[4]), (xf2[5], yf2[5]), (xf2[6], yf2[6]),
             (xf2[7], yf2[7]), (xf2[8], yf2[8]),
             (xf2[9], yf2[9]), (xf2[10], yf2[10]), (xf2[11], yf2[11]),
             (xf2[12], yf2[12]), (xf2[13], yf2[13]), (xf2[14], yf2[14]),
             (xf2[15], yf2[15]), (xf2[16], yf2[16]), (xf2[17], yf2[17]),
             (xf2[18], yf2[18]), (xf2[19], yf2[19]), (xf2[20], yf2[20]),
             (750, 115), (790, 110), (840, 135), (930, 120)
             ])
# рисует первую (самую дальнюю) линию гор, используя для рисования кривых массивы xf1, yf1 и xf2, yf2


def mtn_line2():
    penColor(153, 0, 0)
    brushColor(153, 0, 0)
    polygon([(1000, 300), (0, 350), (0, 245), (5, 245), (25, 265),
             (xf3[0], yf3[0]), (xf3[1], yf3[1]), (xf3[2], yf3[2]),
             (xf3[3], yf3[3]), (xf3[4], yf3[4]), (xf3[5], yf3[5]),
             (xf3[6], yf3[6]), (xf3[7], yf3[7]), (xf3[8], yf3[8]),
             (xf3[9], yf3[9]), (xf3[10], yf3[10]), (175, 240),
             (235, 275), (255, 215), (320, 235), (385, 270), (520, 250),
             (xf4[0], yf4[0]), (xf4[1], yf4[1]), (xf4[2], yf4[2]),
             (xf4[3], yf4[3]), (xf4[4], yf4[4]), (xf4[5], yf4[5]),
             (xf4[6], yf4[6]), (xf4[7], yf4[7]), (xf4[8], yf4[8]),
             (xf4[9], yf4[9]), (xf4[10], yf4[10]), (xf4[11], yf4[11]),
             (750, 250), (800, 210), (835, 235), (860, 205), (930, 210),
             (1000, 160)
             ])
# рисует вторую линию гор, используя для рисвоания кривых массивы xf3, yf3 и xf4, yf4


def sun(xsun, ysun, rsun):
    penColor(255, 255, 0)
    brushColor(255, 255, 0)
    circle(xsun, ysun, rsun)
# рисует солнце с координатами xsun, ysun и радиусом rsun


def mtn_line3():
    penColor(51, 0, 51)
    brushColor(51, 0, 51)
    polygon([(1000, 500), (0, 500), (0, 240), (100, 265), (200, 365),
             (xf5[0], yf5[0]), (xf5[1], yf5[1]), (xf5[2], yf5[2]),
             (xf5[3], yf5[3]), (xf5[4], yf5[4]), (xf5[5], yf5[5]),
             (xf5[6], yf5[6]), (xf5[7], yf5[7]), (xf5[8], yf5[8]),
             (xf5[9], yf5[9]), (650, 435), (675, 450), (xf6[0], yf6[0]),
             (xf6[1], yf6[1]), (xf6[2], yf6[2]), (xf6[3], yf6[3]),
             (xf6[4], yf6[4]), (xf6[5], yf6[5]), (xf6[6], yf6[6]),
             (xf6[7], yf6[7]), (xf6[8], yf6[8]), (xf6[9], yf6[9]),
             (xf6[10], yf6[10]), (xf6[11], yf6[11]), (xf6[12], yf6[12]),
             (xf6[13], yf6[13])
             ])
# рисует третью линию гор, используя для рисования кривых массивы xf5, yf5 и xf6, yf6


canvasSize(1000, 500)
windowSize(1000, 500)
points_filling()
backstage()
mtn_line1()
mtn_line2()
mtn_line3()
sun(475, 95, 50)
penColor(51, 0, 29)
brushColor(51, 0, 29)
bird(750, 400, 1)
bird(650, 330, 0.8)
bird(775, 340, 0.5)
bird(675, 350, 0.5)
bird(475, 207, 0.5)
bird(475, 170, 0.5)
bird(425, 225, 0.5)
bird(415, 160, 0.5)

run()
