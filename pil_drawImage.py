from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def draw_randcolor():
	return (random.randint(137,255), random.randint(137,255), random.randint(137,255))
def draw_randcolor2():
	return (random.randint(50,167), random.randint(50, 167), random.randint(50, 167))
def draw_randchar():
	return chr(random.randint(65, 90))

width, height = 240, 60
image = Image.new('RGB', (width,height), (255, 255, 255))

draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=draw_randcolor())

font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 36)

for t in range(4):
	draw.text((60 * t + 10, 10), draw_randchar(), font = font, fill=draw_randcolor2())

imgage = image.filter(ImageFilter.BLUR)
image.save("code.jpeg", 'jpeg')