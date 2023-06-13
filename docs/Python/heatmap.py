'''this should show a map'''
import numpy as np
import matplotlib.pyplot as plt

# Create a 2D NumPy array of random values
image = np.random.rand(100, 100)

# Display the image using Matplotlib
plt.imshow(image, cmap='gray')
plt.axis('off')  # Hide the axes
plt.show()
