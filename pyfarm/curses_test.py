#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action!!!!!!!!")
myscreen.refresh()
myscreen.getch()

curses.endwin()



import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

def quit():
    """ docstring for quit """
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
