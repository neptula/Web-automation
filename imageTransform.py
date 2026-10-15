#image processing
#flipping image
from PIL import Image
img = Image.open("demo.jpeg")
#transpose method is used to flip the image
trans_img=img.transpose(Image.FLIP_LEFT_RIGHT)
#save it to human readable format
trans_img.save("flipped_demo.jpeg")
print("Image flipped and saved as flipped_demo.jpeg")