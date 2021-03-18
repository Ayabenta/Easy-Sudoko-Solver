#!/usr/bin/env python
# coding: utf-8

# # Solveur sudoku en utilisant l'algorithm de l'exploitation exhaustive  
# 

# En utilisant python, nous avons pu utiliser l'algorithm de labyrinthe, l'exploitation exhaustive, cet algorithme se base principalement sur des cellules qui par la suite doivent êtres visitées un par un.
# Dans ce code nous avons crée une fonction qui affiche la matrice 9*9 en forma du  ligne-colonne-carre, puis la fonction find_empty pour trouver les cellules qui sont vide( ayant un zero),la fonction check pour  valider si le numero ajouter dans une  cellule donnée n'est pas répliqué  dans la ligne concerner, la colonne et le carre, et puis solve pour affecter à chaque cellule le numero adéquat après avoir valider qu'il est unique, dans cette méthode nous avons utiliser l'exploitation exhaustive récursive, ainsi, on peut avancer et trouver des cellule vide les remplir ainsi que pour revenir en arrière et rectifiée les valeurs (les remmetre a zéro). 

# 
# 
# 
# ce travail est fait par :
# Aya Bentaleb 
# Aymane Hmidich
# Hiba Houssam
# Kaoutar El Keddadi.

# In[ ]:


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def show_board(bo) :
    for i in range(len(bo)):
        if i%3 == 0 and i !=0 :
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo)):
            if j%3 == 0 and j !=0 :
                print("|" , end ="")
            if j == 8 :
                print(bo[i][j])
            else :
                print(str(bo[i][j])+" ", end = "")
show_board(board)
                
    


# In[3]:


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


# In[13]:


def check(board, number, position):
   #checking duplicated numbers within a row
    for i in range(9):
        if board[position[0]][i] == number and i != position[1] :
            return False 
   #checking duplicated numbers within a column
    for i in range(9):
        if board[i][position[1]] == number and i != position[0] :
            return False 
    #checking duplicated numbers within a box 
    x_position_box = position[1] // 3
    y_position_box = position[0] // 3
    for i in range(y_position_box*3, y_position_box*3 + 3):
        for j in range(x_position_box*3, x_position_box*3 + 3): 
             if board[i][j] == number and (i,j) != position:
                    return False
    return True
    
    
        


# In[14]:


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# In[15]:


show_board(board)
solve(board)
print("___________________")
show_board(board)


# In[ ]:




