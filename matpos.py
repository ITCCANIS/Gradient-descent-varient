import numpy as np

def classify_matrix(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    if np.all(eigenvalues > 0):
        return "La matrice est definie positive"
    elif np.all(eigenvalues >= 0):
        return "La matrice est semi-definie positive"
    elif np.all(eigenvalues < 0):
        return "La matrice est definie negative"
    elif np.all(eigenvalues <= 0):
        return "La matrice est semi-definie negative"
    else:
        return "La matrice est indefinie"

rows, cols =[int(x) for x in input("enterez la taille de la matrice:").split()]  
matrix= [[int(input())for j in range (cols)]for i in range (rows)]
classify_matrix(matrix)