frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)


cajón = ['documentos', 'sobres', 'lápices']
# acceder al cajón con índice 0 y valor print
print(cajón[0])  # imprime documentos
# acceder al cajón con índice 1 y  valor print
print(cajón[1]) # imprime sobres
# acceder al cajón con índice 2 y valor print
print(cajón[2]) # imprime lápices


x = [1,2,3,4,5]
x.append(99)
print(x)
# la salida sería [1,2,3,4,5,99]