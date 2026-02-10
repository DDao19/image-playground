from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
filteredImg = img.convert("L")
rotatedImg = filteredImg.rotate(90)

rotatedImg.save("rotate.png", "png")
