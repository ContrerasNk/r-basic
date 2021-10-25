import numpy as np

#1
np.arange(5, 121)

#2
np.arange(0,16).reshape((4,4))

#3
np.eye(7)

#4
np.arange(20).reshape((5,4))

#5
np.linspace(0,5,20)

# Vistas
n = np.arange(16).reshape(4,4)
t = n.view()
t[:] = 5
n

# Percentil
x = np.arange(10)
np.percentile(x, q = 200)


