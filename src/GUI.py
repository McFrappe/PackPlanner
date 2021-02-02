import main
from tkinter import *

def new_planner():
    name_label = Label(text="Name:")
    name_entry = Entry(text="Name")
    name_label.grid()
    name_entry.grid()

def render_main():
    main_window = Tk()
    main_window.title("Plan Packer")
    main_window.geometry("500x150")

    btn_new_planner = Button(main_window, text="New planner", width = 10, run = new_planner())
    btn_new_planner.grid(column = 1, row = 0)

    btn_show_content = Button(main_window, text="Show planner", width = 10)
    btn_show_content.grid(column = 2, row = 0)

    btn_add_item = Button(main_window, text="Add item", width = 10)
    btn_add_item.grid(column = 1, row = 1)

    btn_show_incoming = Button(main_window, text="Show incoming", width = 10)
    btn_show_incoming.grid(column = 2, row = 1)

    btn_remove_planner = Button(main_window, text="Remove planner", width = 10)
    btn_remove_planner.grid(column = 1, row = 2)

    btn_remove_item = Button(main_window, text="Remove item", width = 10)
    btn_remove_item.grid(column = 2, row = 2)

    btn_quit = Button(main_window, text="Quit", width = 10)
    btn_quit.grid(column = 1, row = 3)

    main_window.mainloop()


render_main()
