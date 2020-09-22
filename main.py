from tkinter import *

window = Tk()

def configure_window():
    for el in range(0, 32):
        label = Label(window, text=chr(1040 + el))
        label.grid(column=0, row=el)


if __name__ == '__main__':
    configure_window()
    for i in range(1040, 1050):
        print(chr(i))
    window.mainloop()
