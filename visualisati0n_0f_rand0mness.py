from random import randint
import matplotlib.pyplot as plt

image = []
for row in range(50):
    rows = []
    for column in range(50):
        r = randint(0, 155)
        g = randint(0, 255)
        b = randint(0, 255)
        pixel = (r, g, b)
        rows.append(pixel)
    image.append(rows)


plt.imshow(image)
plt.title('Visualisation of randomness')
plt.axis('off')
plt.show()
