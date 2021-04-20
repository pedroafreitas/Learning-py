import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy import stats

#dados
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([0,2,3,5,8,13,21,34,55,89])

#criando a regressão
slope, intercept, valor_r, valor_p, erro_padrao = stats.linregress(x,y)
def linefitline(b):
    return intercept + slope * b
line1 = linefitline(x)

# #gráfico da regressão
plt.scatter(x,y)
plt.plot(x,line1, c = 'g')
plt.show()

# #Calculo e gráfico da média
line2 = np.full(10,[y.mean()])
plt.scatter(x,y)
plt.plot(x,line2, c = 'r')
plt.show()


#Calculo da distância do modelo
differences_line1 = linefitline(x)-y
line1sum = 0
for i in differences_line1:
    line1sum = line1sum + (i*i)
line1sum

#Calculo da distância da média
differences_line2 = line2 - y
line2sum = 0
for i in differences_line2:
    line2sum = line2sum + (i*i)
print(line2sum)

r2 = r2_score(y, linefitline(x))
print('Scikit: {}'.format(r2))