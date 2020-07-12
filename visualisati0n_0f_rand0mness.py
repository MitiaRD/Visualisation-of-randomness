from random import randint
import matplotlib.pyplot as plt

#creating a matrix of values
image = []
for row in range(50):
    rows = []
    for column in range(50):
        #randomly assigning red green and blue values within the range of 0 - 255
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pixel = (r, g, b)
        rows.append(pixel)
    image.append(rows)

#displaying our newly created random pattern
plt.imshow(image)
plt.title('Visualisation of randomness')
plt.axis('off')
plt.show()
