from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import poc


tensor = poc.Tensor()
tensor.train(100,1000)
prediction=tensor.predict("l",100)
print(prediction)
