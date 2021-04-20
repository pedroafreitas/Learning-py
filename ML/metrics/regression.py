import numpy as np
import math

# Calcula a porcentagem de acurácia entre duas listas
def accuracy(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Média quadrada do erro
def mse(actual, predicted):
   sum_error = 0.0
   for i in range(len(actual)):
      error_i = predicted[i] - actual[i]
      sum_error += (error_i ** 2)
   mean_error = sum_error / float(len(actual))
   return math.sqrt(mean_error)

def rmse_simple(actual, predicted):
   return math.sqrt(mse(actual, predicted))

# Raiz quadrada da média de erro
def rmse(actual, predicted):
	square_sum = 0.0
	for i in range(len(actual)):
		error_i = predicted[i] - actual[i]
		square_sum += (error_i ** 2)
	mean_error = square_sum / float(len(actual))
	return math.sqrt(mean_error)

# Média do valor obsoluto
def mae(actual, predicted):
   sum_error = 0.0
   for i in range(len(actual)):
      sum_error += abs(predicted[i] - actual[i])
   return sum_error / float(len(actual))

validation_data = [2, 1]
estimation = [2.3, 1.5]

print("\nAccuracy = {1:.3f} \nMSE = {0:.3f}".format(
   accuracy(validation_data, estimation),
   mse(validation_data, estimation)))

validation_data = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
estimation = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]

print("\n\nMSE = {0:.3f} \nRMSE = {1:.3f} \nMAE = {2:.3f}".format(
   mse(validation_data, estimation),
   rmse(validation_data, estimation),
   mae(validation_data, estimation)))

