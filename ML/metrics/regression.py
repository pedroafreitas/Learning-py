import numpy as np
import math

# Calcula a porcentagem de acurácia entre duas listas
def accuracy(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

def mse(actual, predicted):
   sum_error = 0.0
	for i in range(len(actual)):
		error_i = predicted[i] - actual[i]
		sum_error += (error_i ** 2)
	mean_error = sum_error / float(len(actual))
	return math.sqrt(mean_error)

def rmse(actual, predicted):
   return math.sqrt(mse(actual, predicted))

# Raiz quadrada da média de erro
def rmse(actual, predicted):
	square_sum = 0.0
	for i in range(len(actual)):
		error_i = predicted[i] - actual[i]
		square_sum += (error_i ** 2)
	mean_error = square_sum / float(len(actual))
	return math.sqrt(mean_error)


estimation = [2.3, 1.5]
validation_data = [2, 1]

print("RSME = {0:.2f} \nAccuracy = {1:.2f}".format(rmse(validation_data, estimation),accuracy(validation_data, estimation)))

