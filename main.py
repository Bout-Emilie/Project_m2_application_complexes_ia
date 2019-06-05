from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import poc
import normalize
import constantes


file_training = normalize.Normalize(constantes.data_training)
file_normaliser_training = file_training.normalizer()


file_test = normalize.Normalize(constantes.data_test)
file_normaliser_test = file_test.normalizer()


ia = poc.Tensor()
ia.train(100,1000)
result=ia.predict(1000,100)
print(result)