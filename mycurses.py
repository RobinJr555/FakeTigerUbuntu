#<head>--------------------------------------------------------------------------</head>-#
#@descripiton:RobinJr's personnal TLI interface ofr GreatWork
#@author:RobinJr.
#@firstedit:2018/4/18
#@lastedit :2018/4/18




#<body>--------------------------------------------------------------------------</body>-#
import curses                           #Terminal handling for character-cell displays
import sys,os

# establish a class for handling the tli interface
class MYCursesClass():
    def __init__(self):
        self.startcurses()

    def startcurses(self):
        # get the window object called stdscr
        self.stdscr          = curses.initscr()
        curses.noecho()                 #turn off automatic echoing of keys to the screen
        curses.cbreak()                 #react to keys instantly
        self.stdscr.keypad(True)

    def terminatecurses(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


    def draw_menu(self):
        inputkey = 0
        self.cursor_x = 0
        self.cursor_y = 0

        self.stdscr.clear()
        self.stdscr.refresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        while ( inputkey != ord('q')):
            self.stdscr.clear()
            inputkey = self.stdscr.getch()

        self.terminatecurses()


#<main>--------------------------------------------------------------------------</main>-#
if __name__ == "__main__":
    t = os.system('clear')
    mycurseclass = MYCursesClass()
    mycurseclass.draw_menu()
