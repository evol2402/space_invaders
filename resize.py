from PIL import Image

# Load the original image
original_image = Image.open("./gif/sb.png")

# Resize the image
resized_image = original_image.resize((600,600))  # Set to desired dimensions

# Save the resized image
resized_image.save("./gif/sb.png")
