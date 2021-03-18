import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 45, 30, 20])
items = ["Android Mobile", "Tv's", "Apple Tv's", "Ipads"]
mexplode = [0.2, 0.1, 0.1, 0.5]
plt.pie(y, labels=items, explode=mexplode, shadow=True)
plt.show()
