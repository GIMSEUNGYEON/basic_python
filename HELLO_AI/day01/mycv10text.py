import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread('dong.jpg', cv2.IMREAD_COLOR)

img_pillow = Image.fromarray(img)

fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 24)
draw = ImageDraw.Draw(img_pillow, 'RGBA')
draw.text((330, 130), "마동석", font=font, fill=(255,255,255,255))

img_numpy = np.array(img_pillow)

cv2.imshow('dongsuk', img_numpy)
cv2.waitKey()
cv2.destroyAllWindows()