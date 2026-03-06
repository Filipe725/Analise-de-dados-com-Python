import numpy as np


array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d);
print(np.shape(array_1d))
print(np.ndim(array_1d))

array_2d = np.array([[1, 2, 3], [4, 5, 6], [8, 9, 10]])
print(np.shape(array_2d))
print(np.ndim(array_2d))

arrayFatiado = array_2d[0:3, 1:2]
print(arrayFatiado)

arrayFatiado[0, 0] = 100

print(array_2d)

array_mascara = array_2d > 20
print(array_mascara)

array_mascara = array_2d[array_2d>50]
print(array_mascara)

array_2d = np.add(array_2d, 50)

array_mascara = array_2d[array_2d>50]
print(array_mascara)


array_multiplicacao = np.multiply(array_2d, 50)
print(array_multiplicacao)   

array_divisao = np.divide(array_multiplicacao, 50)
print(array_divisao)

media = np.mean(array_multiplicacao)
print(media)

desvioPadrao = np.std(array_multiplicacao)
print(desvioPadrao)