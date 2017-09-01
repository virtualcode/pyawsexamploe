#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	system("clear")
	print(cmd_string)
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""

x = 0

while x != ord('4'):
	screen = curses.initscr()

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Add AWS user")
	screen.addstr(5, 4, "2 - Delete AWS user")
	screen.addstr(6, 4, "3 - List AWS users")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		username = get_param("Enter the username")
		curses.endwin()
		execute_cmd("aws iam create-user --user-name " + username)
	if x == ord('2'):
		username = get_param("Enter the username")
		curses.endwin()
		execute_cmd("aws iam delete-user --user-name " + username)
	if x == ord('3'):
		curses.endwin()
		execute_cmd("aws iam list-users")

curses.endwin()

