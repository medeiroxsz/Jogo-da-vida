from tkinter import *
import model

cell_size = 10
is_running = False # o jogo começa parado

def start_click(event):
    global is_running, start_button


    if is_running:
        is_running = False
        start_button.configure(text="Iniciar")
    else:
        is_running = True
        start_button.configure(text="Pause")
        update()
        
def clear_click(event):
    global is_running, clear_button, start_button

    if is_running == True:
        is_running = False
        start_button.configure(text="Iniciar")
    for i in range(model.height):
        for j in range(model.width):
            model.grid_model[i][j] = 0
    update()
       
def grid_click(event):
    global cell_size
    i = int(event.y / cell_size)
    j = int(event.x / cell_size)

    if model.grid_model[i][j] == 1:
        model.grid_model[i][j] = 0
        draw_cell(i,j, "white")
    else:
        model.grid_model[i][j] = 1
        draw_cell(i,j, "black")
        
def option_select(event):
    global is_running, start_button, start_choice
    # Vamos parar o jogo antes
    is_running = False
    start_button.configure(text="Iniciar")
    
    # Agora vamos mudar o padrão do jogo
    selection = start_choice.get()
    if selection == "Glider":
        model.load_pattern(model.glider_pattern)
    elif selection == "Glider gun":
        model.load_pattern(model.glider_gun_pattern)
    else:
        model.randomize_grid()
    update()
    
def setup():
    global root, grid_canvas, start_button, clear_button
    global start_choice, start_option
    
    root = Tk()
    grid_canvas = Canvas(root,
                         width = cell_size*model.width,
                         height= cell_size*model.height,
                         bg = "white")


    start_button = Button(root, text="Iniciar", width=20)
    start_button.bind("<Button-1>", start_click)
    clear_button = Button(root, text="Limpar")
    clear_button.bind("<Button-1>", clear_click)
    grid_canvas.bind("<Button-1>", grid_click)

    
    start_choice = StringVar(root)
    start_choice.set("Padrão")
    start_option = OptionMenu(root, start_choice, "Padrão", "Aleatório", "Glider", "Glider gun",command=option_select)
    start_option.config(width=20)
    

    # grid_canvas.pack()
    # start_button.pack()
    # start_option.pack()
    # clear_button.pack()

    grid_canvas.grid(row=0, column=0, columnspan=3)
    start_button.grid(row=1, column=0, sticky=W, padx=10, pady=10)
    start_option.grid(row=1, column=1,padx=10, pady=10)
    clear_button.grid(row=1, column=2, sticky=E, padx=10, pady=10)

def draw_cell(i,j,color):
    global cell_size, grid_canvas
    x = j * cell_size
    y = i * cell_size
    grid_canvas.create_rectangle(
        x, y, x + cell_size, y + cell_size,
        fill=color, outline="lightgrey")

def update():
    global grid_canvas, root, is_running  # mudou aqui!
    grid_canvas.delete(ALL)  # apaga o canvas

    for i in range(model.height):
        for j in range(model.width):
            if model.grid_model[i][j] == 1:
                draw_cell(i, j, "black")

    if is_running:
        model.next_gen()  # próxima geração
        root.after(100, update)  # temporizador
                                        
if __name__ == "__main__":
    model.randomize_grid()
    setup()
    update()
    mainloop()
