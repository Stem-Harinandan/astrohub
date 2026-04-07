import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_img(path):
    img= Image.open(path)
    img=img.convert("RGB")
    arr=np.array(img)
    arr=arr.astype(np.float32)
    return arr

path=["img_1.jpg","img_1.jpg","img_1.jpg"]
images=[]

for i in path:
    img=load_img(i)
    images.append(img)

print("Number of images:", len(images))
print("Type:", type(images[0]))
print("Shape:", images[0].shape)
print(images)
print(images[0].shape, images[1].shape)

stack = np.stack(images, axis=0)

result = np.mean(stack, axis=0)

result = result / result.max()

plt.imshow(result)
plt.axis("off")
plt.title("Mean Stacked Image")
plt.show()