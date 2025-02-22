from PIL import Image

# Open an image
img = Image.open("example.jpg")

# Show the image
img.show()

# Get image size
print(f"Image size: {img.size}")  # Output: (width, height)

# Convert to grayscale
gray_img = img.convert("L")
gray_img.show()
