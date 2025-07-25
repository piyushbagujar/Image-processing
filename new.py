import cv2
import os


folder_path = r"folder1"

# Get all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
image_files.sort()

images = []
width, height = 800, 600 

for file in image_files:
    img_path = os.path.join(folder_path, file)
    img = cv2.imread(img_path)
    if img is not None:
        img = cv2.resize(img, (width, height))
        images.append(img)

if len(images) == 0:
    print("No images found in the folder.")
    exit()


while True:
    for i in range(len(images)):
        img1 = images[i]
        img2 = images[(i + 1) % len(images)]  

        
        for alpha in range(0, 21):
            a = alpha / 20.0
            blended = cv2.addWeighted(img1, 1 - a, img2, a, 0)
            cv2.imshow("Smooth Slideshow", blended)
            if cv2.waitKey(50) & 0xFF == 27:  
                cv2.destroyAllWindows()
                exit()

        
        if cv2.waitKey(1000) & 0xFF == 27:
            cv2.destroyAllWindows()
            exit()

cv2.destroyAllWindows()
