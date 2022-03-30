import numpy as np

arr = np.array(["Apple", "Mango", "Banana", "Mango", "Cherry", "Pear", "Mango"])

print("Index for Mango: ", np.where(arr == 'Mango')[0])