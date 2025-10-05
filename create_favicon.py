from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (32, 32), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Draw a simple sticker-like symbol (a circle with text)
draw.ellipse([2, 2, 30, 30], fill=(255, 200, 0), outline=(0, 0, 0))

# Save as favicon.ico
img.save('favicon.ico')

print("Favicon created successfully!")