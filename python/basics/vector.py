x0, x1, x2 = 1., 2., 3.
bias, w1, w2 = 0.1, 0.3, 0.5

x = [x0, x1, x2]
w = [bias, w1, w2]

# A simple for-loop
z = 0
for i in range(len(x)):
    z += x[i] * w[i]
print(z)

# list comprehensions
z = sum(x_i*w_i for x_i, w_i in zip(x, w))
print(z)

# A vectorized implementation
import numpy as np

x_vec, w_vec = np.array(x), np.array(w)

z = (x_vec.transpose()).dot(w_vec)
print(z)

z = x_vec.dot(w_vec)
print(z)