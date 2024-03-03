from PIL import Image

# Load the image
logo = Image.open('logo.png')  # Make sure to replace 'path_to_your_logo.png' with the actual path to your logo file

# Convert the image to RGBA (if not already in this mode)
logo = logo.convert("RGBA")

# Get the data of the image
data = logo.getdata()

# Change all non-transparent pixels to white
new_data = []
for item in data:
    # Change all pixels that are not transparent to white
    if item[3] != 0:
        new_data.append((255, 255, 255, item[3]))
    else:
        new_data.append(item)

# Update image data
logo.putdata(new_data)

# Save the new image
logo.save('logo_white.png')
