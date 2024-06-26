from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np

# Text settings
text = "Abonnez-vous à ma chaîne ! ✅"
font_size = 24

# Open cat image (placeholder)
cat_image_path = "/mnt/data/cat_image.jpg"
cat_image = Image.open(cat_image_path)

# Prepare the font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Define image size and create a blank image
image_size = (cat_image.width, cat_image.height + 40)  # Additional space for text
final_image = Image.new("RGBA", image_size, (255, 255, 255, 0))
final_image.paste(cat_image, (0, 0))

# Draw text on the image
draw = ImageDraw.Draw(final_image)
text_width, text_height = draw.textsize(text, font=font)
text_position = ((image_size[0] - text_width) // 2, cat_image.height + 5)
draw.text(text_position, text, font=font, fill="black")

# Convert image to array
frames = [np.array(final_image) for _ in range(10)]  # Simulate a short gif

# Save the GIF
gif_path = "/mnt/data/subscribe_cat.gif"
imageio.mimsave(gif_path, frames, duration=0.5)

gif_path
