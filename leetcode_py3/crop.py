import cv2
import os


imagelist = os.listdir("/Users/akaishuushan/Desktop/uber test")
prefix = "/Users/akaishuushan/Desktop/uber test/"

for i, name in enumerate(imagelist):
    if name == ".DS_Store":
        continue
    print(name)
    img_dir = prefix + name
    img = cv2.imread(img_dir)
    crop = img[330:, :]
    cv2.imwrite(prefix+str(i)+".png", crop)


