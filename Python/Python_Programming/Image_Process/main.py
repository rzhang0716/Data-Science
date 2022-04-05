from PIL import Image, ImageFilter

# open the file convert to python file
img = Image.open("pikachu.jpg")

# blur the image (Convert to png to fit the filter)
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("pik.png", "png")
# Smooth the image
smooth_img = img.filter(ImageFilter.SMOOTH)

# Convert the image color
convert_img = img.convert("L")

# Show the image
filtered_img.show()

# Rotate the image
crooked= filtered_img.rotate(90)

# Resize the image
resize = filtered_img.resize((300, 300))

# Crop the image
crop = filtered_img.crop((100,100,400,400))

# Keep the ratio after resize
img.thumbnail((400, 200))