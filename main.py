from tkinter import *
from cell import Cell
import settings
import util


root = Tk()
# Override the settings og the window
root.configure(bg="pink")
root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')
root.title('Mine Sweeper')
root.resizable(False, False)

top_frame = Frame(root, bg='pink',  # changelater
            width=settings.WIDTH,
            height=util.height_prct(25))
top_frame.place(x=0, y=0)

game_title = Label(
        top_frame,
        bg='pink',
        fg='black',
        text='MINESWEEPER GAME',
        font=('', 48),
)

game_title.place(
        x=util.width_prct(22),
        y=0
)
left_frame = Frame(root,
        bg='pink',  # change later
        width=util.width_prct(25), height=util.height_prct(75)
)
left_frame.place(x=0, y=util.height_prct(25))

center_frame = Frame(root,
        bg='pink',  # change later
        width=util.width_prct(75), height=util.height_prct(75)
)
center_frame.place(x=util.width_prct(25),y=util.height_prct(25))

for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
                c = Cell(x, y)
                c.create_btn_object(center_frame)
                c.cell_btn_object.grid(
                        column=x, row=y
                )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place( 
        x=0, y=0
)
Cell.randomize_mines()


# run the window
root.mainloop()
