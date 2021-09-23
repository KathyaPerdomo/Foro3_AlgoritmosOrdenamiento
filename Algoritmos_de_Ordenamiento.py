#Ordenamiento por inserción
def Insertion_sort(Vector):
    for i in range(1,len(Vector)):
        actual = Vector[i]
        j = i
        #Desplazamiento de los elementos de la matriz }
        while j>0 and Vector[j-1]>actual:
            Vector[j]=Vector[j-1]
            j = j-1
        #insertar el elemento en su lugar
        Vector[j]=actual
---------------------------------------------------------------
        
#Ordenamiento de burbuja
def bubble_sort(vector):
    permutation = True
    iteración = 0
    while permutation == True:
        permutation = False
        iteración = iteración + 1
        for actual in range(0, len(vector) - iteración):
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
    return vector 
--------------------------------------------------------------
  
#Ordenamiento de burbuja bidireccional
def cocktail_sort(vector):
    permutation,dirección,actual = True,1,0
    comienzo,fin = 0,len(vector)-2
    while permutation == True:
        permutation = False
        while (actual<fin and dirección==1) or \
        (actual>comienzo and dirección==-1) :
            # Prueba si intercambio
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
            actual = actual + dirección
        # Cambiar la dirección de desplazamiento
        if dirección==1:
            fin = fin - 1
        else:
            comienzo = comienzo + 1
        dirección = -dirección
    return vector
-------------------------------------------------------------
  
#Ordenamiento Gnome
def Gnome_sort(vector):
    i_b,i_i,taille = 1,2,len(vector)
    while i_b < taille:
        if vector[i_b-1] <= vector[i_b]:
            i_b,i_i = i_i, i_i+1
        else:
            vector[i_b-1],vector[i_b] = vector[i_b],vector[i_b-1]
            i_b -= 1
            if i_b == 0:
                i_b,i_i = i_i, i_i+1
    return vector
-------------------------------------------------------------
  
#Ordenamiento por selección
def selection_sort(vector):
    nb = len(vector)
    for actual in range(0,nb):    
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if vector[j] < vector[mas_pequeno] :
                mas_pequeno = j
        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = temp
--------------------------------------------------------------
            
#Ordenamiento peine
import math  
def comb_sort(vector):
    permutación = True
    gap = len(vector)
    while (permutación == True) or  (gap>1):
        permutación = False
        gap = math.floor(gap / 1.3)
        if gap<1: gap = 1
        for actual in range(0, len(vector) - gap):
            if vector[actual] > vector[actual + gap]:
                permutación = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + gap] = \
                vector[actual + gap],vector[actual]
    return vector
-------------------------------------------------------------
  
#Ordenamiento Shell
def tri_insertion(tableau, gap, debut):
    for i in range(gap + debut,len(tableau),gap):
        en_cours = tableau[i]
        j = i
        while j>0 and tableau[j-gap]>en_cours:
            tableau[j]=tableau[j-gap]
            j = j-gap
        tableau[j]=en_cours
 
def tri_shell (tableau):
    for gap in [6,4,3,2,1]:
        for debut in range(0,gap):
            tri_insertion(tableau,gap,debut)
------------------------------------------------------------
            
#Ordenamiento rápido
def quick_sort(vector):
    if not vector:
        return []
    else:
        pivote = vector[-1]
        menor = [x for x in vector     if x <  pivote]
        mas_grande = [x for x in vector[:-1] if x >= pivote]
        return quick_sort(menor) + [pivote] + quick_sort(mas_grande)
------------------------------------------------------------
