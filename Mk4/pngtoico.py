from PIL import Image

filename = r"Jarvis.png"
img = Image.open(filename)
img.save('Jarvis.ico', format='ICO', sizes=[(32, 32)])
