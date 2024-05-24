import itertools
import lista_nombres as ln

for nombre in ln.lista:
    #eliminar todos los pares, osea el 2 , 4 , 6 etc, (ELIMINA NOMBRES, NO USERNAME)
    usernames= []

    for i in range(0,len(ln.lista),2):
        usernames.append(ln.lista[i])


combinations = list(itertools.combinations(usernames, 2))


#  lista que una en un string los  USERNAME de las combinaciones que sea en el formato
# f'@{USERNAME1}  @{USERNAME2}'
combinaciones_formato = []
for comb in combinations:
    combinaciones_formato.append(f'@{comb[0]}  @{comb[1]}')
