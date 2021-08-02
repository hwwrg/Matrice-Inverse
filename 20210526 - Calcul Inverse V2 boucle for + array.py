"""
matrice saisie:
[[2 3]
 [5 7]]
"""

from tkinter import *
import numpy as np

root = Tk()
root.title = "Calcul Inversation de Matrice"
root.geometry("600x300")

def determinant(matrice):
    '''
    Retourne le determinant
    '''
    if len(matrice) == 2 and len(matrice) == 2:
        det = matrice[0][0]*matrice[1][1] - matrice[1][0]*matrice[0][1]
    else:
        det = 0

    return det


def inverse(matrice):
    """
    Inverse la matrice donnée
    """
    det = determinant(matrice)
    if det != 0:
        # Transposotion des deux valeurs
        tmp = matrice[0][0]
        matrice[0][0] = matrice[1][1]
        matrice[1][1] = tmp

        matrice[0][1] *= -1
        matrice[1][0] *= -1

        mati = []
        for ligne in matrice:
            matj = []
            for element in ligne:
                matj.append(element * (1/det))
            mati.append(matj)
        return mati
    else:
        print("Opération impossible. Le determinant est égale à zéro.")


def calcul():
    global matrice

    aStr = a.get("1.0", "end")
    print(aStr)
    """
    2 3
    5 7
    """
    print(type(aStr))               # <class 'str'>

    aList = []
    for i in aStr:
        if i != " ":
            aList.append(i)
    print(aList)                    # ['2', '3', '\n', '5', '7', '\n']

    # numbre de lignes de matrice saisie
    numLigne = aList.count("\n")
    print(numLigne)                 # 2

    # supprime '\n'
##    aList.remove('\n')            # enlève que le premier item trouvé
    aListClean = []
    for i in aList:
        if i != '\n':
            aListClean.append(int(i))
            """
            int() : convertit item en STR à INT, sinon problème sur conversion
            en array, erreur dans calcul déterminant
            'can't multiply sequence by non-int of type 'numpy.str_''
            """
    print(aListClean)               # [2, 3, 5, 7]

    # numbre de colonnes de matrice saisie
    numColonne = len(aListClean) / numLigne
    print("*"*40, type(numColonne)) # <class 'float'>
    numColonne = round(numColonne)  # round() : flaot --> int
    print("*"*40, type(numColonne)) # <class 'int'>
    print(numColonne)               # 2
    print(type(numColonne))         # <class 'int'>

    # list --> list of lists
    aListLists = []
    for i in range(0, numLigne):
        tmp = aListClean[(i*numColonne):((i+1)*numColonne)]
        aListLists.append(tmp)
    print(aListLists)               # [[2, 3], [5, 7]]
    print(type(aListLists))         # <class 'list'>

    # list of lists --> array
    matrice =np.array(aListLists)
    print(matrice)
    """
    [[2 3]
    [5 7]]
    """
    print(type(matrice))            # <class 'numpy.ndarray'>


    # Solution variable dure
    """
    # Récupère la valeur dans text
    aMat = a.get("1.0", "end")

    # Convertit str à list
    list = aMat.split("\n")         # ['2 3', '5 7', '']
    print(list)
    list.remove('')                 # ['2 3', '5 7']

    # Crée 2 listes correspondant 2 ligne de la matrice
    ligne1 = []
    ligne2 = []

    # Convertit les éléments de list à une liste
    for i in list[0]:
        if i != " ":
            ligne1.append(int(i))

    for i in list[1]:
        if i != " ":
            ligne2.append(int(i))
    print(ligne1, ligne2)           # ['2', '3'] ['5', '7']

    # Crée la matrice
    matrice = np.array([[0,0],[0,0]])
    matrice[0][0]=ligne1[0]
    matrice[0][1]=ligne1[1]
    matrice[1][0]=ligne2[0]
    matrice[1][1]=ligne2[1]
    """

    # calculs déterminant et matrice intersée
    res = inverse(matrice)
    det = determinant(matrice)
    print(res, det)                 # [[-7.0, 3.0], [5.0, -2.0]] -1

    # affiche déterminant
    detAffi = Label(root)

    # vide case matrice b
    b.delete('1.0', END)
    # affiche matrice inversée
##    b.insert(END, res)            # affiche en format array

    # affiche item un par un
    for i in range(0, numLigne):
        for j in range(0, numColonne):
            n = int(res[i][j])
            b.insert(END, n)
            b.insert(END, " ")
        b.insert(END, "\n")

    # affiche déterminant
    detAffi = Label(root, text=det, width="10", height="5")
    detAffi.grid(row=0, column=6)



def main():
    global a
    global b

    # Crée Labels et Texts
    aLabel = Label(root, text="A = ")
    a = Text(root, width="20", height="10")
    bLabel = Label(root, text="B = ")
    b = Text(root, width="20", height="10")
    detLabel = Label(root, text="Déterminant = ")

    # Bouton qui exécute 'calcul()'
    inv = Button(root, text="Inversation", command=calcul)
    # Bouton qui ferme la fenêtre
    ex = Button(root, text="Close", command=root.destroy)

    # leurs grid
    aLabel.grid(row=0, column=0)
    a.grid(row=0, column=1)
    bLabel.grid(row=0, column=3)
    b.grid(row=0, column=4)
    detLabel.grid(row=0, column=5)
    detAffi = Label(root, width="10", height="5")
    detAffi.grid(row=0, column=6)

    inv.grid(row=1, column=0, columnspan=3)
    ex.grid(row=1, column=4, columnspan=3)

    root.mainloop()

if __name__ == '__main__':
    main()
