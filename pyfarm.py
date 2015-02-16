#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from pyprocessing import line
from pyprocessing import key
from pyprocessing import background
from pyprocessing import size
from pyprocessing import stroke
from pyprocessing import run
from pyprocessing import text

X = 1000
Y = 1000
U = 10

CENTER = (X/2, Y/2)


def clear():
    background(200)


def show_grid():
    # x axis
    x_lines = X // U
    y_lines = Y // U

    def make_x(x):
        line(x*U, 0, x*U, X)

    def make_y(y):
        line(0, y*U, Y, y*U)

    map(make_x, xrange(0, x_lines))
    map(make_y, xrange(0, y_lines))


def pretty_lines():
    def make_l(x):
        line(x*U, 0, X, x*U)

    lines = X // U
    map(make_l, xrange(0, lines))


class Liner(object):
    def __init__(self, draw):
        stroke(153)
        self.draw = draw


class Dwarf(object):
    def __init__(self, name=u"Urist", x=CENTER[0], y=CENTER[1]):
        self.char = u'☺'
        self.x = x
        self.y = y
        self.speed = 20
        self.timer = self.speed

    def draw(self):
        stroke(53)
        text(self.char, self.x, self.y, U*5, U*5)
        self.tick()

    def tick(self):
        if self.timer == 0:
            self.move = random.choice(((-U, 0), (0, -U), (0, U), (U, 0)))
            self.x += self.move[0]
            self.y += self.move[1]
            self.timer = self.speed
        else:
            self.timer -= 1


def call(obj, method, *args, **kwargs):
    getattr(obj, method)(*args, **kwargs)


def setup():
    size(1000, 1000)
    show_grid()
    global actors
    actors = []

    urist = Dwarf()
    p_liner = Liner(pretty_lines)

    actors.append(urist)
    actors.append(p_liner)


def draw():
    background(200)
    bindings = {
        'H': clear,
        'G': show_grid,
        'L': pretty_lines
    }
    if key.pressed and key.char in bindings.keys():
        bindings[key.char]()

    map(lambda obj: obj.draw(), actors)


run()
