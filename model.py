# Jogo da Vida
# Brenno Medeiros _ DRE 122086439

from random import randint
width = 50             #declara variável largura como global
height = 50            #delcara variável altura como global

# criando a matriz de zeros representa as células mortas
def new_empty_grid():
    global width, height
    grid = []
    for i in range(height):
        grid.append([0] * width)
    return grid

grid_model = new_empty_grid()
next_grid = new_empty_grid()



#contagem das celulas vivas nos vizinhos
def count_neighbors(i,j):
    global grid_model, width, height
    s = 0
    for row in range(i-1, i+2):
        for col in range(j-1, j+2):
            s+= grid_model[row%height][col%width] #
    s-= grid_model[i][j]
    return s
    #problema se estiver no final da matriz e porque conta a celula central

#definição se a célula central ficará viva ou morta, dependendo da quantidade de vizinhos
def next_gen():
    global grid_model,next_grid, width, height
    for i in range(height):
        for j in range(width):
            n = count_neighbors(i,j)
            if n == 3:
                next_grid[i][j] = 1
            elif n!=2:
                next_grid[i][j] = 0
            else:
                next_grid[i][j] = grid_model[i][j]
    temp = grid_model
    grid_model = next_grid
    next_grid = temp

def randomize_grid():
    global grid_model, width, height
    for i in range(height):
        for j in range(width):
            grid_model[i][j] = randint(0,1)
            
            #next_grid[i][j]

def load_pattern(pattern):
    global grid_model, width, height
    # Vamos  pegar a largura e altura do padrão
    pw = len(pattern[0])
    ph = len(pattern)


    # Agora copiamos cada célula do padrão para o grid
    # Também zeramos as que estão fora do padrão
    for i in range(height):
        for j in range(width):
            if i < ph and j < pw:
                grid_model[i][j] = pattern[i][j]
            else:
                grid_model[i][j] = 0

glider_pattern = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
]

glider_gun_pattern = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]


#teste    
if __name__ == "__main__":
    grid_model[1][1] = 1
    #next_gen()
    for row in grid_model:
        print(row)
    print(count_neighbors(0,0))    
        
